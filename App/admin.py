from django.contrib import admin
from .models import ContactDetail, Subscription, Profile
# Register your models here.

admin.site.register(ContactDetail)
admin.site.register(Subscription)
admin.site.register(Profile)