from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id','typeName')



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blogTitle','blogAuthor','blog_createdTime','blog_updatedTime','blogType','get_read_num')


@admin.register(readNum)
class readNumAdmin(admin.ModelAdmin):
    list_display = ('read_num','blogName')