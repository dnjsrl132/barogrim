from django.contrib import admin
from django.urls import path
from blog.views import *
app_name ="blog"

urlpatterns = [
    path('',blog,name='blog'),
    path('newpost/',new_post,name='new_post'),
    path('<int:pk>/',posting,name='posting'),
    path('<int:pk>/remove/',remove_post,name='remove'),
]
