from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import (
    Post, 
    PostView, 
    Category, 
    PostComment,  
    PostLike, 
    Video
)
# Create your views here.

class BlogView(ListView):
    model = Post
    template_name = "blog.html"
    paginate_by = 6
    ordering = ['-created_date']
    
class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        next_post = Post.objects.filter(pk__gt=self.object.pk).order_by('pk').first()
        prev_post = Post.objects.filter(pk__lt=self.object.pk).order_by('-pk').first()
        context['next_post'] = next_post
        context['previous_post'] = prev_post
        return context