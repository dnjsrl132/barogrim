from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from profileapp.views import *

app_name ="profileapp"

urlpatterns = [
    path('create/',ProfileCreateVeiw.as_view(),name='create'),
    path('update/<int:pk>/',ProfileUpdateVeiw.as_view(),name='update'),
]