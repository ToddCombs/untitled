from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    """入口函数"""
    return HttpResponse('<h1>Hellooooooooo World!</h1>')

def personal(request):
    """个人页面"""
    return HttpResponse('<h1>This is my personal page</h1>')