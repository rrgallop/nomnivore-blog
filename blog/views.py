from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog_home.html'  # Template for the blog home page
    context_object_name = 'posts'
    ordering = ['-created_at']  # Show the newest posts first

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # Template for a single post
