from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(LikeCounts)
class LikeCountsAdmin(admin.ModelAdmin):
    list_display = ['content_object','liked_num']


@admin.register(LikeRecord)
class LikeCountsAdmin(admin.ModelAdmin):
    list_display = ['content_object','user']
