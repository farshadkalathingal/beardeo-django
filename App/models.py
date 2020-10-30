from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
import random

from Blog.models import Post

def get_color():
    color_list = ['#cc0000','#cc0066','#0000cc', '#ff6600', '#cc0099', '#660066', '#000080', '#4d0099', '#993366', '#800040', '#cc3300', '#990099']
    #print('A  Random Hex Color Code is :',hex_number)
    return random.choice(color_list)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='profile', blank=True, null=True)
    color = models.CharField(max_length=10)
    slug = models.SlugField(blank=True, null=True, editable=False)
    
    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        if self.slug == None:
            self.slug = slugify(self.user.username, allow_unicode=True)
            self.color = get_color()
        super().save(*args, **kwargs)

    def get_absolute_url(self, *args, **kwargs):
        return reverse()

    @property
    def post(self):
        return Post.objects.filter(author=self.user).count()


@receiver(post_save, sender=User)
def create_or_update_participant(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

class ContactDetail(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(editable=False, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.slug == None:
            self.slug = slugify(self.created_date, allow_unicode=True)
        super().save(*args, **kwargs)
    
class Subscription(models.Model):
    email = models.EmailField(max_length=150)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email