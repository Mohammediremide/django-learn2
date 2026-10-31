from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'blog_name': "My learning blog",
        'author': "Student author",
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

