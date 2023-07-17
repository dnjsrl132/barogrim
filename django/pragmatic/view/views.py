from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from view.models import CivitTest, Product
from django.urls import reverse

# Create your views here.
def vew(request):
    posts=CivitTest.objects.all()
    return render(request,'view/vew.html',context={'posts':posts})


def upload(request):
    if request.method == 'POST':
        post=Product()
        post.user_id=request.POST['user_id']
        post.imgfile=request.FILES['image']
        post.save()
        posts=CivitTest.objects.all()
        return render(request,'view/vew.html',context={'posts':posts})

    else :
        post=Product()
        return render(request,'view/upload.html',context={'posts':post})

