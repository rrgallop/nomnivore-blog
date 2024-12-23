from django.shortcuts import render
from blog.models import Post

def home_view(request):
    recent_posts = Post.objects.order_by('-created_at')[:3]  # Get the latest 3 posts
    return render(request, 'home.html', {'recent_posts': recent_posts})