from django.contrib import admin
from django.urls import path
from view.views import vew, upload

app_name ="view"

urlpatterns = [
    path('vew/',vew,name='vew'),
    path('upload/',upload,name='upload'),
]
