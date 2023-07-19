from django.contrib import admin
from django.urls import path
from blog.views import *
app_name ="blog"

urlpatterns = [
    path('',blog,name='blog'),
    path('<int:pk>/',posting,name='posting'),
]
