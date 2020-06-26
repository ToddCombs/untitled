from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    """入口函数"""
    # return HttpResponse('<h1>Hellooooooooo World!</h1>')
    return render(request, 'app/index1.html')  # 路径从templates下一层开始写

def personal(request):
    """个人页面"""
    return HttpResponse('<h1>This is my personal page</h1>')

def login(request):
    """扒了简书的登录页，未包含css内容"""
    return render(request, 'app/login.html')