from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from view.models import CivitTest, Product
from django.urls import reverse
from pragmatic.exif import Exif

def vew(request):
    posts=CivitTest.objects.all()
    return render(request,'view/vew.html',context={'posts':posts})

def vewing(request):
    posts=Product.objects.all()
    return render(request,'view/viewing.html',context={'posts':posts})

def upload(request):
    if request.method == 'POST':
        post=Product()
        post.user_id=request.POST['user_id']
        post.imgfile=request.FILES['image']
        post.name='https://127.0.0.1:8000/media/'+str(post.imgfile)
        post.save()
        Exif(post.name,post.user_id)
        posts=CivitTest.objects.all()
        return render(request,'view/viewing.html',context={'posts':posts})

    else :
        post=Product()
        return render(request,'view/upload.html',context={'posts':post})

