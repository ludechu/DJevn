from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
import os
print('工作路径----',os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from . import models
# Create your views here.
def login(request):

    name = models.objects.all

    # return HttpResponse("hello u input num is:%s"%num)
    return render(request, 'login/login.html', {'name':name})

def detail(request,num):

    name = models.student.objects.get(id=num)
    # return HttpResponse("hello u input num is:%s"%num)
    return render(request, 'login/detail.html', {'name': name})

from .models import t_api
def  index(request):
    list = t_api.apiQuery1.all()
    return HttpResponse("这是首页！%s"%list[0])
import random
def randomstr(num=6):
    list = random.sample('qwertyuio@#$%^&',int(num))
    s = ''.join(list)
    return s

def addapi(request):
    for i in range(50):
        newApi = t_api.addapi.create_api(Name=randomstr())
        try:
            newApi.save()
            print("添加：",randomstr())
        except:
            print("添加失败")
    return HttpResponse("添加完成")

def get1(request):
    """get获取浏览器传递的参数"""
    a = request.GET.get('a')
    b = request.GET['b']
    c = request.GET.get('c')
    return HttpResponse("get1页面"+"参数a:"+a+"参数b"+b+"参数c"+c)
def get2(request):
    """http://127.0.0.1:8000/login1/get2/?a=1&a=2&c=3"""
    list = request.GET.getlist('a')
    a1 = list[0]
    a2 = list[1]
    c = request.GET.get('c')
    return HttpResponse("get1页面" + "参数a1:" + a1 + "参数a2" + a2 + "参数c" + c)


def login1(request):
    res = HttpResponse()
    cookie = res.set_cookie("ldc","123456")
    # cookie1 = res.delete_cookie("ldc")
    return HttpResponse("aaa")

def postpage(request):
    return render(request, "post.html")

def post1(request):
    """post获取浏览器提交数据实例"""
    name = request.POST['name']
    hobby = request.POST.getlist('hobby')
    return HttpResponse(name+hobby[0])

def setcookie(request):
    """设置cookie"""
    res = HttpResponse()
    res.set_cookie("ldc","123456")
    return HttpResponse("Cookie设置成功")
def getcookie(request):
    """获取cookie"""
    res = HttpResponse()
    cookie = request.COOKIES
    return HttpResponse("获取cookie:%s" % cookie['ldc'])
def delcookie(request):
    """删除cookie"""
    res = HttpResponse()
    res.delete_cookie('ldc')
    return HttpResponse("cookie删除成功")

def redirect(request):
    """重定向"""
    return HttpResponseRedirect('/login1/redirect1')
def redirect1(request):

    return HttpResponse("这是重定向后的视图")

def main(request):
    return render(request, 'login/main.html')

def login_index(request):
    return render(request,'login/login_index.html')










