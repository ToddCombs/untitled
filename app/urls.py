# Author:ToddCombs
from django.conf.urls import url
from django.urls import path

from app import views

urlpatterns = [
    # path('personal', views.personal),
    url('personal', views.personal),
    url('index', views.index),
    url('login', views.login),
]
