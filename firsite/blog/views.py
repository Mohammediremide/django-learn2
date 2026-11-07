from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def home(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})