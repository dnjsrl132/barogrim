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
        return redirect('/blog/')
    return render(request,'blog/new_post.html')