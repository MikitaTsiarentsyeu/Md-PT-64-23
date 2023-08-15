from django.shortcuts import render, HttpResponse, redirect
import datetime
from .models import Post, Author
from .forms import AddPost, AddPostModel
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import permission_required


def show_first_post(request):
    post = Post.objects.all()[0]
    return render(request, 'test.html', {"post": post})

def show_second_post(request):
    post = Post.objects.all()[1]
    return render(request, 'test.html', {"post": post})
    
def show_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        viewed_posts = request.session.get('vp', [])
        if post.id not in viewed_posts:
            viewed_posts.append(post.id)
        request.session['vp'] = viewed_posts
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
    viewed_posts = request.session.get('vp', [])
    return render(request, 'posts.html', {'posts':posts, 'viewed_posts': viewed_posts})

@permission_required('app.add_post')
def add_post(request):
    if request.method == 'POST':
        form = AddPostModel(request.POST, request.FILES)
        if form.is_valid():
            # post_item = Post()
            # post_item.author = Author.objects.all()[0]
            # post_item.issued = datetime.datetime.now()
            # post_item.title = form.cleaned_data['title']
            # post_item.content = form.cleaned_data['content']
            # post_item.post_type = form.cleaned_data['post_type']
            # post_item.image = form.cleaned_data['image']
            # post_item.save()

            post_item = form.save(False)
            post_item.author = Author.objects.get(email=request.user.email)
            post_item.issued = datetime.datetime.now()
            post_item.save()
            # form.save_m2m()
            return redirect('post', post_item.id)
    else:
        form = AddPostModel()
    
    return render(request, 'add_post.html', {"form":form})