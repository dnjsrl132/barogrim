from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin
from articleapp.forms import *
from articleapp.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from articleapp.decorators import *
from commentapp.forms import CommentCreationForm
# Create your views here.

@method_decorator(login_required,'get')
@method_decorator(login_required,'post')
class ArticleCrateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        temp_article=form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail',kwargs={'pk':self.object.pk})
    
class ArticleDetailView(DetailView, FormMixin):
    model = Article
    form_class = CommentCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'

@method_decorator(article_ownership_required,'get')
@method_decorator(article_ownership_required,'post')
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/update.html'
    def form_valid(self, form):
        no_instance=self.object.image
        instance=form.save(commit=False)
        if no_instance != self.request.FILES:
            no_instance.delete()
        else:
            instance.image=no_instance
        instance.save()
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('articleapp:detail',kwargs={'pk':self.object.pk})


@method_decorator(article_ownership_required,'get')
@method_decorator(article_ownership_required,'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'

class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/list.html'
    paginate_by = 25