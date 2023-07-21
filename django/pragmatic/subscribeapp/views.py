from typing import Any, Optional
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, RedirectView
from django.views.generic.edit import FormMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from articleapp.forms import *
from subscribeapp.models import *
from articleapp.decorators import *

from commentapp.forms import CommentCreationForm
# Create your views here.

@method_decorator(login_required,'get')
class SubscriptionView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail',kwargs={'pk':self.request.GET.get('project_pk')})
    def get(self,request,*args,**kwargs):
        project=get_object_or_404(Project,pk=self.request.GET.get('project_pk'))
        user=self.request.user

        subscription = Subscription.objects.filter(user=user,project=project)
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user,project=project).save()
        return super(SubscriptionView,self).get(request,*args, **kwargs)

class SubscriptionListView(ListView):
    model=Article
    context_object_name='article_list'
    template_name="subscribeapp/list.html"
    paginate_by=5

    def get_queryset(self):
        projects=Subscription.objects.filter(user=self.request.user).values_list('project')
        article_list=Article.objects.filter(project__in=projects)
        return article_list