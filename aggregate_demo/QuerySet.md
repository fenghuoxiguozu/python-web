##�ۺϺ���

***�ۺϺ�����Ҫ����һЩ����ִ�оۺϺ����ķ���������ȥִ�С�����aggregate, annotate***

- aggregate ��ȫ��������Ĳ�ѯ������һ���ֵ�
- annotate �Ƿ����ѯ������QuerySet����  

###Methods
  
  - Avg
  - Sum
  - Count
  - Max
  - Min
  - F���ʽ:��̬�Ļ�ȡĳ���ֶ��ϵ�ֵ���������F���ʽ������������ȥ���ݿ��в�ѯ���ݣ����൱��ֻ����һ����ʶ�����á�
    ������Ҫ��ԭ��ÿ��ͼ��ļ۸���ԭ���Ļ���֮������10Ԫ����ô����ʹ�����´�����ʵ�֣�
       ` Book.objects.update(price=F("price")+10)`
  - Q���ʽ��ʹ��`Q`���ʽ������ѯ����������������֮����ж��ֲ�������/��|��~�ȣ��Ӷ�ʵ��һЩ���ӵĲ�ѯ������
    ��ȡ�۸����100������ͼ�������в������������ֵ�ͼ�飺
       `Book.objects.filter(Q(price__gte=100)&~Q(name__icontains="��"))`
    

    
## QuerySet.API
  - all ����
  - filter ����
  - exclude ȥ��
  - get
  - update ����
  - order_by :���ǰ������Ĺ�������ң���ʹ�ú��������ʽ
      `Article.objects.order_by("create_time").order_by("author__name")`
    ����������ߵ����ֽ������򣬶�����ʹ�����µĴ���ʱ�䡣
  - values ��ʾ��Ҫ���ֶ�,����QuerySet����,��װ����dict
	``` 
	Book.objects.values('id','name') 
	>>> {"id":"XX","name":"xx"}    
	```
  - values_list ��ʾ��Ҫ���ֶ�,����QuerySet����,��װ����tuple
  	``` 
	Book.objects.values('id','name') 
	>>> ("id":"XX","name":"xx")    
	```
  - selectz_related
  - prefetch_related
