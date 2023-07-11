from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return render(request,'accountapp/hello_world.html')
    #return HttpResponse('hello world!')
# Create your views here.
