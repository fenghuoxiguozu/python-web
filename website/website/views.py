from django.shortcuts import render,redirect
from django.contrib import auth
from django.urls import reverse
from .forms import LoginForm

def index(request):
    return render(request,'index.html')


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
