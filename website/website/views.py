 from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import LoginForm,RegisterForm
from django.http import JsonResponse,HttpResponse

def index(request):
    # return render(request,'index.html')
    return JsonResponse({"code":"SUCCESS"})


def login(request):
    # username = request.POST.get('username','')
    # password = request.POST.get('password', '')
    # user = auth.authenticate(request,username=username,password=password)
    # referer=request.META.get('HTTP_REFERER',reverse('index'))
    # if user is not None:
    #     auth.login(request,user)
    #     return redirect(referer)
    # else:
    #     return render(request,'login.html',{"message":"false"})
    if request.method=='POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user=login_form.cleaned_data['user']
            auth.login(request,user)
            return redirect(request.GET.get('from',reverse('index')))
    else:
        login_form=LoginForm()
    context={}
    context['login_form']=login_form
    return render(request,'login.html',context)


def register(request):
    if request.method=='POST':
        reg_form=RegisterForm(request.POST)
        if reg_form.is_valid():
            username=reg_form.cleaned_data['username']
            email=reg_form.cleaned_data['email']
            password=reg_form.cleaned_data['password']
            # 创建用户
            user=User.objects.create_user(username,email,password)
            user.save()
            # 登录用户
            user=auth.authenticate(username=username,password=password)
            auth.login(request,user)
            return redirect(request.GET.get('from',reverse('home')))

    else:
        reg_form=RegisterForm()
    context={}
    context['reg_form']=reg_form
    return render(request,'register.html',context)