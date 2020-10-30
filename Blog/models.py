from django.db import models
from django.contrib.auth.models import User
from tinymce_4.fields import TinyMCEModelField
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True, null=True, editable=False)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.slug == None:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self, *args, **kwargs):
        return reverse("category-blogs", kwargs={"slug": self.slug})

class Post(models.Model):
    number = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = TinyMCEModelField()
    thumbnail = models.ImageField(upload_to='blogs')
    popular = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    update_date = models.DateTimeField(default=timezone.now, editable=False)
    #likes = models.IntegerField(default=15)
    tags = models.ManyToManyField(Category)
    slug = models.SlugField(max_length=350 ,blank=True, null=True, editable=False)


    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_date = timezone.now()
        if not self.slug:
            self.slug = slugify(self.title +'-'+ str(self.created_date), allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self, *args, **kwargs):
        return reverse("blog-details", kwargs={"slug": self.slug})

    def get_absolute_author(self):
        return reverse("profile", kwargs={"slug": self.author.profile.slug})

    @property
    def views(self):
        return PostView.objects.filter(post=self).count()

    @property
    def likes(self):
        return PostLike.objects.filter(post=self)

    @property
    def comments(self):
        return self.comments.all()

@receiver(post_save, sender=Post)
def update_posts(sender, instance, created, **kwargs):
    if created:
        count = Post.objects.all().count()
        instance.number = count
        instance.slug = slugify(instance.title +'-'+ str(instance.created_date), allow_unicode=True)
        instance.save()

    

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class PostComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.user.username

class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username


class Video(models.Model):
    title = models.CharField(max_length=150)
    thumbnail = models.ImageField(upload_to='blogs')
    url = models.URLField(max_length=200)
    created_date = models.DateTimeField(editable=False)
    slug = models.SlugField(blank=True, null=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_date = timezone.now()
        if not self.slug:
            self.slug = slugify(self.created_date, allow_unicode=True)
        super().save(*args, **kwargs)