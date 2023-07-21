from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from accountapp.forms import AccountUppdateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accountapp.decorators import account_ownership_required

has_ownership = [login_required, account_ownership_required]
# Create your views here.


class AccountCreateView(CreateView):
    model=User
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'accountapp/create.html'

@method_decorator(has_ownership,name='get')
@method_decorator(has_ownership,name='post')
class AccountUpdateView(UpdateView):
    model=User
    form_class = AccountUppdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('home')
    template_name = 'accountapp/update.html'


class AccountDetailView(DetailView,MultipleObjectMixin):
    model=User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'
    paginate_by = 25
    def get_context_data(self, **kwargs):
        object_list=Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView,self).get_context_data(object_list=object_list,**kwargs)

@method_decorator(has_ownership,name='get')
@method_decorator(has_ownership,name='post')
class AccountDeleteView(DeleteView):
    model=User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
