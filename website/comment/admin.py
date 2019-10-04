from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('commentUser','commentTime','content_object','commentText')
