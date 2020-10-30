from django import forms
from .models import ContactDetail, Subscription

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactDetail
        fields = ("name", "email", "message")

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ("email",)