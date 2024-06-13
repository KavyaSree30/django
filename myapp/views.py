# myapp/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import BlogPost, Comment
from .forms import CommentForm, PostForm, RegistrationForm

def index(request):
    posts = BlogPost.objects.all()
    return render(request, 'myapp/index.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return HttpResponseRedirect(reverse('myapp:post_detail', args=[post.id]))
    else:
        form = CommentForm()
    return render(request, 'myapp/post_detail.html', {'post': post, 'comments': comments, 'form': form})

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('myapp:index'))
    else:
        form = PostForm()
    return render(request, 'myapp/add_post.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('myapp:index')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('myapp:index')

def search(request):
    query = request.GET.get('q')
    results = BlogPost.objects.filter(title__icontains=query) if query else None
    return render(request, 'myapp/search_results.html', {'results': results, 'query': query})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('myapp:index')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
