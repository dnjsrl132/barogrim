from django.contrib import admin
from django.urls import path
from view.views import vew, upload, delete
app_name ="view"

urlpatterns = [
    path('vew/',vew,name='vew'),
    path('upload/',upload,name='upload'),
    path('delete/',delete,name='delete'),
]
