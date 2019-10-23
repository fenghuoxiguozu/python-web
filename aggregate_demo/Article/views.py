from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.db.models import Avg,Count,Sum,Max,Min,F,Q
from .models import Book,Sales,Publisher,Author

#返回所有图书的平均定价   aggregate AVG
def index1(request):
    result=Book.objects.aggregate(Avg('price'))
    print(result)   #{'price__avg': 65.5} 字典
    print(connection.queries)
    return HttpResponse('index1')

#返回所有图书的平均售出价格  annotate  AVG
def index2(request):
    # 返回QuerySet
    results=Book.objects.annotate(avg=Avg('sales__price'))
    for result in results:
        print("%s -- %s"%(result.name,result.avg))
        '''
        水浒传 -- 42.5
        三国演义 -- 55.0
        西游记 -- 57.5
        红楼梦 -- 67.5
        '''
    return HttpResponse('index2')

#返回所有图书的数量  Count
def index3(request):
    result= Book.objects.aggregate(Count('id'))
    print(result)
    return HttpResponse('index3')

#返回年龄的不重复数量 distinct
def index4(request):
    result= Author.objects.aggregate(Count('age',distinct=True))
    print(result)
    return HttpResponse('index4')

#返回每本书的销量 Sum
def index5(request):
    results= Book.objects.annotate(sale_num=Sum('sales__num'))
    for result in results:
        print("%s--%s"%(result.name,result.sale_num))
    return HttpResponse('index5')

#返回作者年龄信息  Max,Min
def index6(request):
    result= Author.objects.aggregate(max_age=Max('age'),min_age=Min('age'))
    print(result['max_age'],result['min_age'])
    return HttpResponse('index6')

#给每本书定价增加5元  F表达式
def index7(request):
    Book.objects.update(price=F('price')+5)
    # print("%s--%s" % (result.name, result.price))
    return HttpResponse('index7')

#获取字段name和字段author相同的数据  F表达式
def index8(request):
    results=Book.objects.filter(name=F('author'))
    if len(results)>0:  #有相同数据
        for result in results:
            print(result)
    else:               #没有相同数据
        print("name和author没有相等数据")
    return HttpResponse('index8')

#返回评分大于4.6并且价格小于90；   Q表达式 ~Q取反
def index9(request):
    results1= Book.objects.filter(rate__gt=4.6,price__lt=90)
    # 或者：results1 = Book.objects.filter(Q(rate__gt=4.6) & Q(price__lt=90))
    for result in results1:
        print("%s--%s--%s" % (result.name, result.rate,result.price))
    print("返回评分大于4.6或者价格小于80")
    results2 = Book.objects.filter(Q(rate__gt=4.6) | Q(price__lt=80))
    for result in results2:
        print("%s--%s--%s" % (result.name, result.rate, result.price))
    print("包含评分大于4.6,名称 包含‘’的信息")
    results3 = Book.objects.filter(Q(rate__gt=4.6) & Q(name__contains='西'))
    for result in results3:
        print("%s--%s--%s" % (result.name, result.rate, result.price))
    return HttpResponse('index9')


