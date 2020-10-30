from django.shortcuts import redirect, render
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import FormView
# Create your views here.
from .forms import ContactForm, SubscriptionForm
from Blog.models import (
    Post
)
from .models import Profile

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(popular=True)[:4]
        return context
    
    def post(self, request, *args, **kwargs):
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


class AboutView(TemplateView):
    template_name = "about.html"

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["followers_count"] = len(Follow.objects.followers(self.object.user))
        # if self.request.user.is_authenticated:
        #     context["followers"] = Follow.objects.following(self.request.user)
        #     context["blocked"] = Block.objects.blocking(self.request.user)
        return context