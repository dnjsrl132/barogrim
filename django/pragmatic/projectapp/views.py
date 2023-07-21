from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.list import MultipleObjectMixin
from commentapp.forms import CommentCreationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from articleapp.models import Article

from projectapp.decorators import *
from projectapp.forms import *
from projectapp.models import *

# Create your views here.

@method_decorator(login_required,'get')
@method_decorator(login_required,'post')
class ProjectCrateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail',kwargs={'pk':self.object.pk})
    
class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'
    paginate_by = 25
    def get_context_data(self, **kwargs):
        object_list=Article.objects.filter(project=self.get_object())
        return super(ProjectDetailView,self).get_context_data(object_list=object_list,**kwargs)

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 25