from django.shortcuts import render,get_object_or_404,render_to_response
from .models import *
from django.core.paginator import Paginator

# 文字列表页/首页
def blog_list(request):
    context = {}
    all_blogs=Blog.objects.all()

    paginator=Paginator(all_blogs,3)
    page_num=request.GET.get('page',1)
    pages_of_blogs=paginator.page(page_num)


    context['blogs']= pages_of_blogs
    context['names'] = BlogType.objects.all()
    return render_to_response('blog_list.html',context)

# 文字详情页
def blog_detail(request,blog_id):
    context = {}
    context['blog'] = get_object_or_404(Blog,id=blog_id)
    context['names'] = BlogType.objects.all()
    return render_to_response('blog_detail.html', context)

# 分类列表页
def blog_type(request,blogType_id):
    context = {}
    blogTypes=get_object_or_404(BlogType,id=blogType_id)
    context['blogs'] = Blog.objects.filter(blogType=blogTypes)
    context['blog_type']=blogTypes  #分类标题（e.g. django）
    context['names'] = BlogType.objects.all()  #右侧分类标签
    return render_to_response('blog_type.html',context)

# def sidebar(request):
#     context = {}
#     context['names'] = BlogType.objects.all()
#     return render_to_response('index.html',context)

