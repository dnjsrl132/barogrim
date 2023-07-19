from django.shortcuts import redirect, render
from blog.models import Post

# Create your views here.
'''def index(request):
    return render(request, 'blog/index.html')
'''
def blog(request):
    postlist=Post.objects.all()
    return render(request,'blog/blog.html',{'postlist':postlist})
def posting(request, pk):
    post=Post.objects.get(pk=pk)
    return render(request,'blog/posting.html',{'post':post})
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