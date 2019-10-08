from django.shortcuts import render,redirect
from django.contrib.contenttypes.models import ContentType
from .models import *
from django.urls import reverse
from .forms import CommentForm
from django.http import JsonResponse

# Create your views here.

def update_comment(request):
    # refer =request.META.get("HTTP_REFERER",reverse('index'))
    # if not request.user.is_authenticated:
    #     return render(request,'error.html',{"message":"请先登录","redirect_to":refer})
    # text=request.POST.get('text','')
    # if text=="":
    #     return render(request,'error.html',{"message":"评论内容为空","redirect_to":refer})
    # try:
    #     content_type = request.POST.get('content_type', '')
    #     object_id = int(request.POST.get('object_id', ''))
    #     model_class=ContentType.objects.get(model=content_type).model_class()
    #     model_obj=model_class.objects.get(id=object_id)
    # except Exception as e:
    #     return render(request,'error.html',{"message":"评论对象不存在","redirect_to":refer})
    #
    #
    # comment=Comment()        # comment.commentUser=request.user
        # comment.commentText=text
        # comment.content_object=model_obj
        # comment.save()
        # return redirect(refer)

        refer = request.META.get("HTTP_REFERER", reverse('index'))
        comment_form = CommentForm(request.POST,user=request.user)
        data={}
        if comment_form.is_valid():
            # 检查通过保存数据
            comment = Comment()
            comment.commentUser = comment_form.cleaned_data['user']
            comment.commentText = comment_form.cleaned_data['text']
            comment.content_object = comment_form.cleaned_data['content_object']
            comment.save()

            # 返回Ajax数据
            data['status']='SUCCESS'
            data['username']=comment.commentUser.username
            data['comment_time']=comment.commentTime.strftime('%Y-%m-%d %H:%M:%S')
            data['text']=comment.commentText
        else:
            data['status']='ERROR'
            data['message']=list(comment_form.errors.values())[0][0]
        return JsonResponse(data)



