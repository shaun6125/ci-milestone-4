import os
import json
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from django.contrib.auth import login
from django.contrib.auth.models import User
from . import models
from datetime import timedelta

# Load environment variables from env.py
DOMAIN = os.environ.get('STRIPE_DOMAIN', 'http://localhost:8000')  # Default to localhost if not set
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')  # Set Stripe API key

def membership(request) -> HttpResponse:
    # We login a sample user for the demo.
    user, created = User.objects.get_or_create(
        username='Shaun', email="craven6622@googlemail.com"
    )
    if created:
        user.set_password('password')
        user.save()

    # Log the user in and explicitly specify the backend
    login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # Specify the backend here

    return render(request, 'membership.html')

def cancel(request) -> HttpResponse:
    return render(request, 'cancel.html')

def success(request) -> HttpResponse:
    # Capture the session ID from the URL query string
    stripe_checkout_session_id = request.GET.get('session_id')

    if not stripe_checkout_session_id:
        return HttpResponse("Session ID is missing.", status=400)

    try:
        # Fetch the checkout session from Stripe using the session_id
        checkout_session = stripe.checkout.Session.retrieve(stripe_checkout_session_id)

        # Optionally, you can perform additional logic here, such as storing session details in your database.

        # You can also render the success page with session details or user data
        return render(request, 'success.html', {'session_id': stripe_checkout_session_id})
    
    except stripe.error.StripeError as e:
        # Handle any Stripe-related errors
        return HttpResponse(f"Stripe error: {str(e)}", status=500)

def create_checkout_session(request) -> HttpResponse:
    price_lookup_key = request.POST['price_lookup_key']
    try:
        prices = stripe.Price.list(lookup_keys=[price_lookup_key], expand=['data.product'])
        price_item = prices.data[0]

        # Create a checkout session for a subscription
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {'price': price_item.id, 'quantity': 1},
            ],
            mode='subscription',  # Use 'subscription' mode for memberships
            success_url=DOMAIN + reverse('success') + '?session_id={CHECKOUT_SESSION_ID}',  # Success URL includes session ID
            cancel_url=DOMAIN + reverse('cancel')
        )

        # Record the checkout session in the database for the current user
        models.CheckoutSessionRecord.objects.create(
            user=request.user,
            stripe_checkout_session_id=checkout_session.id,
            stripe_price_id=price_item.id,
        )

        return redirect(
            checkout_session.url,  # Redirect the user to the Stripe checkout page
            code=303
        )
    except Exception as e:
        print(e)
        return HttpResponse("Server error", status=500)

def direct_to_customer_portal(request) -> HttpResponse:
    """
    Creates a customer portal for the user to manage their subscription.
    """
    checkout_record = models.CheckoutSessionRecord.objects.filter(
        user=request.user
    ).last()  # For demo purposes, we get the last checkout session record the user created.

    checkout_session = stripe.checkout.Session.retrieve(checkout_record.stripe_checkout_session_id)

    portal_session = stripe.billing_portal.Session.create(
        customer=checkout_session.customer,
        return_url=DOMAIN + reverse('membership')  # Send the user here from the portal.
    )
    return redirect(portal_session.url, code=303)

@csrf_exempt
def collect_stripe_webhook(request) -> JsonResponse:
    """
    Stripe sends webhook events to this endpoint.
    We verify the webhook signature and update the database record.
    """
    webhook_secret = os.environ.get('STRIPE_WH_SECRET_MEMBERSHIP')
    signature = request.META["HTTP_STRIPE_SIGNATURE"]
    payload = request.body

    try:
        event = stripe.Webhook.construct_event(
            payload=payload, sig_header=signature, secret=webhook_secret
        )
    except ValueError as e:  # Invalid payload.
        raise ValueError(e)
    except stripe.error.SignatureVerificationError as e:  # Invalid signature
        raise stripe.error.SignatureVerificationError(e)

    _update_record(event)

    return JsonResponse({'status': 'success'})

def _update_record(webhook_event) -> None:
    """
    We update our database record based on the webhook event.

    Use these events to update your database records.
    You could extend this to send emails, update user records, set up different access levels, etc.
    """
    data_object = webhook_event['data']['object']
    event_type = webhook_event['type']

    if event_type == 'checkout.session.completed':
        # Fetch the CheckoutSessionRecord associated with this session
        checkout_record = models.CheckoutSessionRecord.objects.get(
            stripe_checkout_session_id=data_object['id']
        )
        
        # Update the session record with the Stripe customer and subscription details
        checkout_record.stripe_customer_id = data_object['customer']
        checkout_record.has_access = True
        checkout_record.is_completed = True
        checkout_record.plan_name = data_object['line_items']['data'][0]['description']  # Plan name
        checkout_record.start_date = data_object['payment_succeeded']  # Assuming the `created` field is when the subscription starts
        # You may need to calculate the end date based on your subscription model, for example, a 30-day subscription
        checkout_record.end_date = checkout_record.start_date + timedelta(days=30)  # Example of setting an end date
        
        checkout_record.save()
        print('🔔 Payment succeeded!')
    elif event_type == 'customer.invoice.payment_succeeded':
        print('🎟️ Subscription created')
    elif event_type == 'customer.invoice.updated':
        print('✍️ Subscription updated')
    elif event_type == 'customer.invoice.deleted':
        # Handle subscription cancellation (if necessary)
        checkout_record = models.CheckoutSessionRecord.objects.get(
            stripe_customer_id=data_object['customer']
        )
        checkout_record.has_access = False
        checkout_record.save()
        print('✋ Subscription canceled: %s', data_object.id)

def update_subscription_status(user, checkout_session):
    # Find or create the CheckoutSessionRecord related to the user
    record, created = CheckoutSessionRecord.objects.get_or_create(user=user, session_id=checkout_session.id)
    
    # Set the access flag to True after payment is confirmed
    if checkout_session.status == 'paid':  # Example condition
        record.has_access = True
        record.save()




