# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import timezone
from .models import Post
from .forms import PostForm, BoardSearchForm
from django.db.models import ProtectedError
from django.views.generic.edit import FormView
from .forms import BoardSearchForm

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    form = BoardSearchForm()
    return render(request, 'board/post_list.html', {'posts': posts, 'form':form})

def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'board/post_detail.html', { 'post':post })
#
# def post_single(request, pk):
    posts = Post.objects.filter(pk__gt=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'board/post_single.html', { 'post':post, 'posts': posts })

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.modified_date = timezone.now()
            post.save()
            return redirect('board:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'board/post_edit.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.modified_date = timezone.now()
            post.save()
            return redirect('board:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'board/post_edit.html', {'form':form})

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author == request.user:
        post.delete()
        return redirect('board:post_list')


def search(request):
    # if request.method == 'GET':
    #     form = BoardSearchForm(request.GET)
    #     if 'search_word' in request.GET:
    #         results = Post.objects.filter(text__contains = request.GET['search_word'])
    #     return render(request, 'board/post_search.html', {'results': results})
    # else:
    #     form = BoardSearchForm()
    # return render(request, 'board/post_search.html',{'form':form} )
    if 'search_word' in request.GET and request.GET['search_word']:
        sWord = request.GET['search_word']
        results = Post.objects.filter(text__icontains = sWord)
        return render(request, 'board/post_search.html', {'results': results, 'query': sWord})
    else:
        return HttpResponse('검색어를 입력 해 주세요.')

