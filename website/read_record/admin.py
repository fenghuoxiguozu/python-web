from django.contrib import admin
from .models import *

@admin.register(readNum)
class readNumAdmin(admin.ModelAdmin):
    list_display = ('read_num','content_object')

@admin.register(readDetail)
class readDetailAdmin(admin.ModelAdmin):
    list_display = ('date','read_num','content_object')