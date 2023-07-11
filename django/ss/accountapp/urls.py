from django.urls import path
from accountapp.views import hello_world

app_name = "acountapp"

#"acountapp:hello_world"

urlpatterns = [
    path('hello_world/',hello_world)
]