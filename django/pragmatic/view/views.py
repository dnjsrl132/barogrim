import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from view.models import CivitTest, Product
from django.urls import reverse
from view.exif import Exif


def vew(request):
    posts=CivitTest.objects.all()
    '''pots=CivitTest.objects.get(user_id="qwe")
    url=pots.user
    os.remove(os.path.join(settings.MEDIA_ROOT,url))
    pots.delete()'''
    return render(request,'view/vew.html',context={'posts':posts})

def delete(request):
    if request.method == 'POST':
        name=request.POST['user_id']
        pots=CivitTest.objects.get(user_id=name)
        os.remove(os.path.join(settings.MEDIA_ROOT,pots.user_id))
        pots.delete()
        return HttpResponseRedirect(reverse('view:vew'))
    else :
        return render(request,'view/delete.html')

def upload(request):
    if request.method == 'POST':
        post=Product()
        post.user_id=request.POST['user_id']
        post.imgfile=request.FILES['image']
        post.name='media/'+str(post.imgfile)
        post.save()
        Exif(post.name,post.user_id)
        return HttpResponseRedirect(reverse('view:vew'))
    else :
        post=Product()
        return render(request,'view/upload.html',context={'posts':post})

