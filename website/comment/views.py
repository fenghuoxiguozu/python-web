from django.shortcuts import render,redirect
from django.contrib.contenttypes.models import ContentType
from .models import *
from django.urls import reverse

# Create your views here.

def update_comment(request):
    user=request.user
    text=request.POST.get('text','')
    content_type = request.POST.get('content_type', '')
    object_id = int(request.POST.get('object_id', ''))
    model_class=ContentType.objects.get(model=content_type).model_class()
    model_obj=model_class.objects.get(id=object_id)

    comment=Comment()
    comment.commentUser=user
    comment.commentText=text
    comment.content_object=model_obj
    comment.save()

    refer =request.META.get("HTTP_REFERER",reverse('index'))
    return redirect(refer)
