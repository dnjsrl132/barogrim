import base64
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from view.models import CivitTest
from django.urls import reverse
from view.exif import Exif
from PIL import Image
from PIL.ExifTags import TAGS


def vew(request):
    posts=CivitTest.objects.all()
    for post in posts:
        post.img=str(post.img).replace("b\'","")[:-1]
    return render(request,'view/vew.html',context={'posts':posts})

def delete(request):
    if request.method == 'POST':
        name=request.POST['user_id']
        if name == "all" :
            pots=CivitTest.objects.all()
        else:
            pots=CivitTest.objects.get(user_id=name)
        pots.delete()
        return HttpResponseRedirect(reverse('view:vew'))
    else :
        return render(request,'view/delete.html')

def upload(request):
    if request.method == 'POST':
        user_id=request.POST['user_id']
        img_file=request.FILES['image']
        encode=base64.b64encode(img_file.read()).decode('utf-8')
        image=Image.open(img_file)
        Exif(image,user_id,str(img_file),encode)
        return HttpResponseRedirect(reverse('view:vew'))
    else :
        return render(request,'view/upload.html')

