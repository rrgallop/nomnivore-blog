from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),  # List of all posts
    path('<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),  # Single post
]