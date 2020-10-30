from django.contrib import admin

# Register your models here.
from .models import (
    Post, 
    PostView, 
    Category, 
    PostComment,  
    PostLike, 
    Video
)
# Register your models here.

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(PostLike)
admin.site.register(PostView)
admin.site.register(Video)