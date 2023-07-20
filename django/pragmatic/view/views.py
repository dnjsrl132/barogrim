import base64
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from view.models import CivitTest
from django.urls import reverse
from view.exif import Exif
from PIL import Image
from PIL.ExifTags import TAGS
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms.models import model_to_dict

def vew(request):
    posts=CivitTest.objects.all()
    for post in posts:
        post.img=str(post.img).replace("b\'","")[:-1]
    return render(request,'view/vew.html',context={'posts':posts})

def vewing(request,user_id):
    post=CivitTest.objects.get(user_id=user_id)
    post.img=str(post.img).replace("b\'","")[:-1]
    post_dict=model_to_dict(post)
    temp=post_dict['user_id']
    post_dict['user_id']=post_dict['name']
    post_dict['name']=temp
    return render(request,'view/vewing.html',{'post':post_dict})

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

@login_required
def upload(request):
    if request.method == 'POST':
        user_id=request.user.username
        img_file=request.FILES['image']
        encode=base64.b64encode(img_file.read()).decode('utf-8')
        image=Image.open(img_file)
        Exif(image,user_id,str(img_file).replace(".jpg",""),encode)
        return HttpResponseRedirect(reverse('view:vew'))
    else :
        return render(request,'view/upload.html')

