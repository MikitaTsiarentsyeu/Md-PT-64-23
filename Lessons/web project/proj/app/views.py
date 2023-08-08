from django.shortcuts import render, HttpResponse
import datetime
from .models import Post
from django.http import HttpResponseNotFound

def show_first_post(request):
    post = Post.objects.all()[0]
    return render(request, 'test.html', {"post": post})

def show_second_post(request):
    post = Post.objects.all()[1]
    return render(request, 'test.html', {"post": post})
    
def show_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        return render(request, 'post.html', {"post": post})
    except:
        return HttpResponseNotFound()

def show_all_posts(request):
    posts = Post.objects.all()
    # post_list = ""
    # for post in posts:
    #     post_list = f"{post_list}<li>{post.title}</li>"
    # response = f"<h1>Posts:</h1><ul>{post_list}</ul>"
    # return HttpResponse(response)
    return render(request, 'posts.html', {'posts':posts})