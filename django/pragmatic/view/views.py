from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from view.models import CivitTest
from django.urls import reverse

# Create your views here.
def vew(request):
    posts=CivitTest.objects.all()
    return render(request,'view/vew.html',context={'posts':posts})

def upload(request):
    return HttpResponseRedirect(reverse('view:upload'))