import datetime
from read_record.models import *
from blog.models import  Blog
from django.utils import timezone
from django.db.models import Sum
from django.contrib.contenttypes.models import ContentType
from django.db.models import Count


def once_read(request,obj):
    ct = ContentType.objects.get_for_model(obj)
    key='%s_%s_read' % (ct.model,obj.id)

    if not request.COOKIES.get(key):
        # 总阅读数+1
        TotalNum,created1=readNum.objects.get_or_create(content_type=ct,object_id=obj.id)
        TotalNum.read_num += 1
        TotalNum.save()
        # 当天阅读数+1
        date=timezone.now().date()
        DateNum,created2= readDetail.objects.get_or_create(content_type=ct, object_id=obj.id,date=date)
        DateNum.read_num += 1
        DateNum.save()
    return key


# def get_7days_readNum(content_type):
# #     today=timezone.now().date()
# #     read_nums=[]
# #     for i in range(7,0,-1):
# #         date=today-datetime.timedelta(days=i)
# #         read_details=readDetail.objects.filter(content_type=content_type,date=date)
# #         result=read_details.aggregate(read_num_sums=Sum('read_num'))    #{'read_num_sums':2}
# #         read_nums.append(result['read_num_sums'] or 0)
# #     read_seven_sums= sum(read_nums)
# #     return read_seven_sums

def get_todays_readNum(content_type):
    today=timezone.now().date()
    read_details=readDetail.objects.filter(content_type=content_type,date=today)
    result=read_details.aggregate(read_num_sums=Sum('read_num'))    #{'read_num_sums':2}
    # read_nums.append(result['read_num_sums'] or 0)
    # read_seven_sums= sum(read_nums)
    return result

def get_7days_hot_blogs():
    today = timezone.now().date()
    seven_days=today-datetime.timedelta(days=7)
    blogs = Blog.objects.filter(read_details__date__lt=today, read_details__date__gt=seven_days).\
        values('id','blogTitle').annotate(seven_hot_blogs=Sum('read_details__read_num')).order_by('-seven_hot_blogs')
    return blogs[:5]


