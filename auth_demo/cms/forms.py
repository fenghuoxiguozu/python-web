from django import forms
from utils.forms import FormMixin
from django.core import validators

class LoginForm(forms.Form,FormMixin):
    telephone=forms.CharField(max_length=11,error_messages={"max_length":"请输入正确格式的手机号码","min_length":"请输入正确格式的手机号码"},validators=[validators.RegexValidator(r'1[345678]\d{9}',message="请输入正确格式的手机号码")])
    password=forms.CharField(max_length=12,min_length=6,error_messages={"max_length":"密码不能超过12位","min_length":"密码不能少于6位"})
    remember=forms.IntegerField(required=False)

