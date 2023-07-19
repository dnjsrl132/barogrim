from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from accountapp.models import HelloWorld
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accountapp.forms import AccountUppdateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accountapp.decorators import account_ownership_required

has_ownership = [login_required, account_ownership_required]
# Create your views here.
@login_required
def hello_world(request):
    if request.method =="POST":
        temp=request.POST.get('hello_world_input')
        trear=request.POST.get('pw')

        new_hello_world=HelloWorld()
        new_hello_world.text=temp
        #new_hello_world.password=trear
        new_hello_world.save()

        hello_world_list=HelloWorld.objects.all()
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
        #return render(request,'accountapp/hello_world.html',context={'hello_world_list':hello_world_list})
    else:
        hello_world_list=HelloWorld.objects.all()
        return render(request,'accountapp/hello_world.html',context={'hello_world_list':hello_world_list})


class AccountCreateView(CreateView):
    model=User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

@method_decorator(has_ownership,name='get')
@method_decorator(has_ownership,name='post')
class AccountUpdateView(UpdateView):
    model=User
    form_class = AccountUppdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'


class AccountDetailView(DetailView):
    model=User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

@method_decorator(has_ownership,name='get')
@method_decorator(has_ownership,name='post')
class AccountDeleteView(DeleteView):
    model=User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
