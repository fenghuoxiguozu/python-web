from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.views.generic import View
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.http import require_POST,require_GET
from .forms import LoginForm
from utils import restful

# Create your views here.

class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request, 'login.html',context={"form":form})

    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user=authenticate(request,username=telephone,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    if remember:
                        request.session.set_expiry(None)
                    else:
                        request.session.set_expiry(0)
                    # return restful.ok(message="成功登陆")
                    return redirect('/')
                else:
                    return restful.auth_error(message="账号被冻结")
            else:
                return restful.params_error(message="账号或密码错误")
        else:
            errors=form.get_errors()
            return restful.params_error(message=errors)

        # return render(request, 'login.html',context={"form":form})
