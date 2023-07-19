from django.contrib import admin
from django.urls import path
from view.views import *
app_name ="view"

urlpatterns = [
    path('vew/',vew,name='vew'),
    path('vew/<slug:user_id>/',vewing,name='vew'),
    path('upload/',upload,name='upload'),
    path('delete/',delete,name='delete'),
]
