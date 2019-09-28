
# from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('',blog_list,name="blog_list"),
    path('<int:blog_id>',blog_detail,name="blog_detail" ),
    path('type=<int:blogType_id>',blog_type,name="blog_type" ),
]
