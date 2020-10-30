from django.urls import path

from .views import (
  BlogView,
  BlogDetailView
)

urlpatterns = [
    path('', BlogView.as_view(), name="blog-home"),
    path('<slug>/', BlogDetailView.as_view(), name="blog-details"),
]
