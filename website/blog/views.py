from django.shortcuts import render,get_object_or_404,render_to_response
from .models import *

# 文字列表页/首页
def blog_list(request):
    context={}
    context['blogs']=Blog.objects.all()
    print(context['typeNames'])
    return render_to_response('blog_list.html',context)

# 文字详情页
def blog_detail(request,blog_id):
    context = {}
    context['blog'] = get_object_or_404(Blog,id=blog_id)
    return render_to_response('blog_detail.html', context)

# 分类列表页
def blog_type(request,blogType_id):
    context = {}
    blogTypes=get_object_or_404(BlogType,id=blogType_id)
    context['blogs'] = Blog.objects.filter(blogType=blogTypes)
    context['blog_type']=blogTypes  #分类标题（e.g. django）
    return render_to_response('blog_type.html',context)

# def right_bar(requests):
#     context = {}
#     context['blog_type'] = BlogType.objects.all()

