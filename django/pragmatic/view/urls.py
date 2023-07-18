from django.contrib import admin
from django.urls import path
from view.views import vew, upload, delete, vewing
app_name ="view"

urlpatterns = [
    path('vew/',vew,name='vew'),
    path('vewing/',vewing,name='vewing'),
    path('upload/',upload,name='upload'),
    path('delete/',delete,name='delete'),
]
