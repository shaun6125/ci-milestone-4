from django.db import models
from django.contrib.auth.models import User

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
