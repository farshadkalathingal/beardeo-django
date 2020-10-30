from django.urls import path

from .views import (
    HomeView,
    AboutView,
    ContactView,
    ProfileView
)

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('profile/<slug>/', ProfileView.as_view(), name="profile"),
]
