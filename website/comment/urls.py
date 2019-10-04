
from django.contrib import admin
from django.urls import path,include
from blog.views import *
from django.conf import settings
from django.conf.urls.static import  static
from website.views import login,index
from .views import *


urlpatterns = [
    path('update_comment',update_comment,name='update_comment'),
    # path('ckeditor',include('ckeditor_uploader.urls')),
    # path('admin/', admin.site.urls),
    # path('blog/',include('blog.urls')),
    # path('login/',login,name="login"),
]

