from django.urls import path,include
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

app_name='App'

urlpatterns = [
    path('', views.index,name='index'),
]