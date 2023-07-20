from django.shortcuts import redirect, render
from blog.models import *
from django.contrib.auth.decorators import login_required
from django import forms
from blog.forms import CommentForm
# Create your views here.
'''def index(request):
    return render(request, 'blog/index.html')
'''
def blog(request):
    postlist=Post.objects.all()
    return render(request,'blog/blog.html',{'postlist':postlist})
def posting(request, pk):
    post=Post.objects.get(pk=pk)
    comments=Comment.objects.get(post=post)
    return render(request,'blog/posting.html',{'post':post,'comments':comments})
def new_post(request):
    if request.method =='POST':
        Post.objects.create(postname=request.POST['postname'],contents=request.POST['contents'])
        return redirect('/blog/')
    return render(request,'blog/newposting.html')
def remove_post(request,pk):
    post=Post.objects.get(pk=pk)
    if request.method =='POST':
        post.delete()
        return redirect('/blog/')
    return render(request,'blog/deleteposting.html',{'Post':post})

@login_required
def comments_create(request,pk):
    if request.user.is_authenticated:
        post=Post.objects.get(pk=pk)
        comment_form=request.POST['content']
        Comment.objects.create(post=post,user=request.user,content=comment_form)
        return redirect('blog:posting',post.pk)
    return render(request,'blog/posting.html',{'post':post})

@login_required
def comments_delete(request,post_pk,com_pk):
    if request.user.is_authenticated:
        comment=Comment.objects.get(pk=com_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('blog:posting',post_pk)