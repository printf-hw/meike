from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pymysql

from meikeapp.models import Admin
from meikeapp.models import User
from meikeapp.models import News
from django.shortcuts import HttpResponse
from django.http import JsonResponse

from meikeapp import spider
# Create your views here.
def login(request):

    if request.method == 'POST':
        uname =request.POST.get("uname")
        pwd=request.POST.get("upwd")
        c=Admin.objects.filter(uname=uname,password=pwd)
        if c.__len__()==0:
            c = User.objects.filter(uname=uname, password=pwd)
            if c.__len__() == 0:
                return render(request, 'login.html', {"msg": "用户名或密码错误"})
            else:
                # request.session["uname"] = uname
                return render(request, 'index.html', {})
            return render(request, 'login.html', {"msg":"用户名或密码错误"})
        else:
            # request.session["uname"]=uname
            newslist=spider.getnews()
            return render(request, 'mng.html', {"newslist":newslist})


    else:
        return render(request,'login.html',{})


def index(req):
        newslist = News.objects.all()
        return render(req,'index.html', {"newslist":newslist})
def register(request):
    if request.method == 'POST':
        uname =request.POST.get("uname")
        pwd=request.POST.get("upwd")
        c = User.objects.filter(uname=uname)
        if c.__len__()==0:
            User.objects.create(uname=uname,password=pwd).save()
            return HttpResponse('注册成功')

        else:
            return render(request, 'register.html', {"msg": "用户名已存在"})
    else:

        return render(request, 'register.html', {})

@csrf_exempt
def recode(req):
    url=req.POST.get("url")
    title=req.POST.get("title")
    News.objects.create(url=url,title=title,uname="_admin",content='1',time='1',source='1').save()
    return JsonResponse("成功",safe=False)
def recodelist(req):
    newslist=News.objects.all()
    return render(req,"recodelist.html",{"newslist":newslist})
def delete(req):
    id=req.POST.get("id")
    News.objects.filter(id=id).delete()
    return JsonResponse("成功",safe=False)
