# Author:ToddCombs
from django.conf.urls import url
from django.urls import path

from app import views

urlpatterns = [
    # path('personal', views.personal),
    url('index', views.index),
    url('personal', views.personal),
    url('cure', views.cure),
    url('alter', views.alter),
    url('update', views.update),
    url('delete', views.delete),
    url('addb', views.addb),
    url('login', views.login),
    url('login1', views.loginview),

]
