/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// Retrieve the Stripe public key and client secret from the page
var stripePublicKey = JSON.parse(document.getElementById('id_stripe_public_key').textContent);
var clientSecret = JSON.parse(document.getElementById('id_client_secret').textContent);

// Initialize Stripe with the public key
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

// Set up the style for the card input field
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

// Create an instance of the card element
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle real-time validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();

    // Disable the card input and submit button while processing
    card.update({ 'disabled': true });
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeIn(100);

    // Gather the form data and additional information for the request
    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();  // CSRF token for security

    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };

    var url = '/checkout/cache_checkout_data/';  // Endpoint for cache_checkout_data view

    // Send the post request to cache checkout data
    $.post(url, postData).done(function () {
        // Proceed with confirming the payment using Stripe's confirmCardPayment method
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county.value),
                }
            },
        }).then(function(result) {
            if (result.error) {
                // Handle errors and re-enable the form if payment fails
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeOut(100);
                card.update({ 'disabled': false });
                $('#submit-button').attr('disabled', false);
            } else if (result.paymentIntent.status === 'requires_action' || result.paymentIntent.status === 'requires_source_action') {
                // Handle additional authentication like 3D Secure
                stripe.confirmCardPayment(result.paymentIntent.client_secret).then(function(confirmResult) {
                    if (confirmResult.error) {
                        // Handle error if authentication fails
                        alert('Authentication failed. Please try again.');
                    } else if (confirmResult.paymentIntent.status === 'succeeded') {
                        form.submit();  // Submit the form to complete the checkout
                    }
                });
            } else if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        });
    }).fail(function () {
        // If the request to cache checkout data fails, reload the page
        alert('There was an issue processing your payment data. Please try again.');
        location.reload();
    });
});
