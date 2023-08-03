from django.shortcuts import render
import datetime
from .models import Post

def show_first_post(request):
    post = Post.objects.all()[0]
    return render(request, 'test.html', {"post": post})

def show_second_post(request):
    post = Post.objects.all()[1]
    return render(request, 'test.html', {"post": post})
    
def show_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'test.html', {"post": post})

def show_all_posts(request):
    pass