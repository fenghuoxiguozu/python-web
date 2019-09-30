from django.shortcuts import render,get_object_or_404,render_to_response
from .models import *
from django.core.paginator import Paginator
from django.db.models import Count


def sidebar(request):
    context = {}
    # 博客类型分类
    context['right_typeNames'] = BlogType.objects.annotate(typeCount=Count('blog'))
    # context['right_typeNames'] = BlogType.objects.all()
    # context['TypeNums']=BlogType.objects.annotate(typeCount=Count('blog'))
    # 博客按月份分类
    context['right_Dates'] = Blog.objects.dates('blog_createdTime','month',order='DESC')
    return context


def Pages(request,Blogs):
    paginator = Paginator(Blogs, 3)
    page_num = request.GET.get('page', 1)
    pages_of_blogs = paginator.page(page_num)
    return pages_of_blogs

# 博客列表页
def blog_list(request):
    Blogs=Blog.objects.all()
    context=sidebar(request)    #右侧分类标签
    context['Blogs'] = Blogs    #所有博客
    context['pageBlogs']= Pages(request,Blogs)  #分页博客
    return render_to_response('blog_list.html',context)

# 分类列表页
def blog_with_type(request,blogType_id):
    context = sidebar(request)  #右侧分类标签
    blogTypes=get_object_or_404(BlogType,id=blogType_id)
    Blogs= Blog.objects.filter(blogType=blogTypes)
    context['blogs'] = Blogs
    context['blog_type']=blogTypes  #分类标题（e.g. django）
    context['pageBlogs'] = Pages(request, Blogs)  # 分页博客
    return render_to_response('blog_with_type.html', context)

# 日期归档
def blog_with_date(request,year,month):
    context = sidebar(request)  # 右侧分类标签
    Blogs=Blog.objects.filter(blog_createdTime__year=year,
                                 blog_createdTime__month=month)
    context['blogs_with_dates'] =Blogs
    context['pageBlogs'] = Pages(request, Blogs)  # 分页博客
    return render_to_response('blog_with_data.html',context)


# 博客详情页
def blog_detail(request,blog_id):
    context = {}
    blog=get_object_or_404(Blog,id=blog_id)
    context['blog']=blog
    context['names'] = BlogType.objects.all()
    # 上下篇博客筛选
    context['pre_blog']= Blog.objects.filter(blog_createdTime__lt=blog.blog_createdTime).first()
    context['next_blog'] = Blog.objects.filter(blog_createdTime__gt=blog.blog_createdTime).last()
    return render_to_response('blog_detail.html', context)