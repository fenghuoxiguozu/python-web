import datetime
from read_record.models import *
from django.utils import timezone
from django.db.models import Sum
from django.contrib.contenttypes.models import ContentType


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


def get_seven_days_readNum(content_type):
    today=timezone.now().date()
    read_nums=[]
    for i in range(6,-1,-1):
        date=today-datetime.timedelta(days=i)
        read_details=readDetail.objects.filter(content_type=content_type,date=date)
        result=read_details.aggregate(read_num_sums=Sum('read_num'))
        read_nums.append(result['read_num_sums'] or 0)
    read_seven_sums= sum(read_nums)
    return read_seven_sums

def get_hot(content_type):
    today = timezone.now().date()
    read_details = readDetail.objects.filter(content_type=content_type, date=today).order_by('-read_num')
    return read_details


