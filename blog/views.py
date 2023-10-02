from django.shortcuts import render
from .models import BlogPost

# Create your views here.

def posts(request):
    posts = BlogPost.objects.all()
    context = {'posts': posts}
    return render(request, 'posts.html', context)