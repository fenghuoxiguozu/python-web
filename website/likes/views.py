from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from .models import *

# Create your views here.

# def like_change(request):
#     #获取数据
#     content_type=request.Get.get('content_type')
#     object_id=request.Get.get('object_id')
#     is_like = request.Get.get('is_like')
#     user=request.user
#
#     #处理数据
#     if is_like=='true':
#         #要点赞
#         like_count,created=LikeRecord.objects.get_or_create(content_type=content_type,object_id=object_id,user=user)
#         if created:
#             # 未点赞过
#             like_count, created = LikeRecord.objects.get_or_create(content_type=content_type, object_id=object_id)
#             like_count.like_num+=1
#             like_count.save()
#             # 点赞过，不能重复
#     else:
#         #取消点赞
#         if LikeCounts
#             if LikeRecord.objects.filter(content_type=content_type, object_id=object_id,user=user).exists()





