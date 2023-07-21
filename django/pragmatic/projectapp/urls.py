from django.urls import path
from django.views.generic import TemplateView

from projectapp.views import *

app_name ="projectapp"

urlpatterns = [
    path('list/',ProjectListView.as_view(), name='list'),
    
    path('create/',ProjectCrateView.as_view(), name='create'),
    path('detail/<int:pk>',ProjectDetailView.as_view(), name='detail'),

    #path('delete/<int:pk>',ProjectDeleteView.as_view(), name='delete'),
]