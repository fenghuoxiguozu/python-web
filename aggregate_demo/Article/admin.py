from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','age')

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name','price','rate','pages','author','publisher')



@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ('name','price','num','end_time')
