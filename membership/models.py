from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.plan_name


class CheckoutSessionRecord(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, help_text="The user who initiated the checkout."
    )
    stripe_customer_id = models.CharField(max_length=255)
    stripe_checkout_session_id = models.CharField(max_length=255)
    stripe_price_id = models.CharField(max_length=255)
    has_access = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    plan_name = models.CharField(max_length=100, blank=True, null=True)  # Store the plan's name
    start_date = models.DateField(blank=True, null=True)  # Subscription start date
    end_date = models.DateField(blank=True, null=True)  # Subscription end date

    def __str__(self):
        return f"Checkout session for {self.user.username} ({self.stripe_checkout_session_id})"
    
    def set_subscription_details(self, plan_name, start_date, end_date):
        """
        Method to set the subscription details after successful payment.
        """
        self.plan_name = plan_name
        self.start_date = start_date
        self.end_date = end_date
        self.has_access = True
        self.is_completed = True
        self.save()

    @classmethod
    def update_or_create_subscription(cls, user, session):
        """
        Creates or updates the CheckoutSessionRecord with subscription details
        after a successful Stripe checkout session.
        """
        plan_name = session['line_items']['data'][0]['description']
        start_date = timezone.now().date()
        end_date = start_date + timedelta(days=365)  # Example: set a 1-year duration
        
        record, created = cls.objects.update_or_create(
            user=user,
            stripe_checkout_session_id=session['id'],
            defaults={
                'stripe_customer_id': session['customer'],
                'stripe_price_id': session['line_items']['data'][0]['price']['id'],
                'has_access': True,
                'is_completed': True,
                'plan_name': plan_name,
                'start_date': start_date,
                'end_date': end_date
            }
        )
        return record


# This function will be triggered after a successful Stripe webhook
def stripe_webhook(request):
    """
    This is your Stripe webhook handler. Ensure to verify the webhook signature 
    and handle the 'checkout.session.completed' event properly.
    """
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    endpoint_secret = settings.STRIPE_WH_SECRET_MEMBERSHIP
    event = None

    
    try:
        # Verify the webhook signature
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret)

        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            user_id = session['customer']
            user = User.objects.get(id=user_id)

            # Update or create the CheckoutSessionRecord
            record = CheckoutSessionRecord.update_or_create_subscription(
                user, session)

            return JsonResponse({"status": "success"}), 200

    except stripe.error.SignatureVerificationError:
        return JsonResponse({"status": "error", "message": "Invalid signature"}), 400
    
    except Exception as e:
        print(f"Error processing webhook: {e}")
        return JsonResponse({"status": "error", "message": str(e)}), 500
