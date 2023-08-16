
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from articleapp.views import ArticleListView

urlpatterns = [
    path('',ArticleListView.as_view(),name='home'),
    path('admin/', admin.site.urls),
    path('account/',include('accountapp.urls')),
    path('accounts/',include('allauth.urls')),
    path('view/',include('view.urls')),
    path('profiles/',include('profileapp.urls')),
    path('articles/',include('articleapp.urls')),
    path('comments/',include('commentapp.urls')),
    path('subscribe/',include('subscribeapp.urls')),
    path('projects/',include('projectapp.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)