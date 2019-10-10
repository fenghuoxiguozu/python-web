from django.shortcuts import render,redirect
from django.contrib.contenttypes.models import ContentType
from .models import *
from django.urls import reverse
from .forms import CommentForm
from django.http import JsonResponse

# Create your views here.

def update_comment(request):
        refer = request.META.get("HTTP_REFERER", reverse('index'))
        comment_form = CommentForm(request.POST,user=request.user)
        data={}
        if comment_form.is_valid():
            # 检查通过保存数据
            comment = Comment()
            comment.commentUser = comment_form.cleaned_data['user']
            comment.commentText = comment_form.cleaned_data['text']
            comment.content_object = comment_form.cleaned_data['content_object']

            parent=comment_form.cleaned_data['parent']
            if not parent is None:
                comment.root=parent.root if not parent.root is None else parent
                comment.parent = parent
                comment.reply_to=parent.commentUser
            comment.save()

            # 返回Ajax数据
            data['status']='SUCCESS'
            data['username']=comment.commentUser.username
            data['comment_time']=comment.commentTime.strftime('%Y-%m-%d %H:%M:%S')
            data['text']=comment.commentText

            if not parent is None:
                data['reply_to']=comment.reply_to.username
            else:
                data['reply_to']=''
            data['id']=comment.id

        else:
            data['status']='ERROR'
            data['message']=list(comment_form.errors.values())[0][0]
        return JsonResponse(data)



