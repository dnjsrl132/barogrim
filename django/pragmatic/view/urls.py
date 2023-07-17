from django.contrib import admin
from django.urls import path
from view.views import vew, upload, vewing

app_name ="view"

urlpatterns = [
    path('vew/',vew,name='vew'),
    path('viewing/',vewing,name='viewing'),
    path('upload/',upload,name='upload'),
]
