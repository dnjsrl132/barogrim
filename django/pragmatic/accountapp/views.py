from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('hello world!')
# Create your views here.
