"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

import app
from app import views, urls


# path方法调用的是python第三方模块或框架,不能用正则表达式。可以使用re_path编写正则表达式
# 而url则是自定义的模块,旧版本使用url方法多一些，更偏向本地
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    # url方法使用时应注意不带反斜杠
    url('app', include(app.urls)),
    # path方法使用时应注意需要加反斜杠
    # path('app/', include(app.urls)),

]
