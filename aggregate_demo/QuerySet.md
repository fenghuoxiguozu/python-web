##聚合函数

***聚合函数需要放在一些可以执行聚合函数的方法下面中去执行。比如aggregate, annotate***

- aggregate 是全部结果集的查询，返回一个字典
- annotate 是分组查询，返回QuerySet对象  

###Methods
  
  - Avg
  - Sum
  - Count
  - Max
  - Min
  - F表达式:动态的获取某个字段上的值。并且这个F表达式，不会真正的去数据库中查询数据，他相当于只是起一个标识的作用。
    比如想要将原来每本图书的价格都在原来的基础之上增加10元，那么可以使用以下代码来实现：
       ` Book.objects.update(price=F("price")+10)`
  - Q表达式：使用`Q`表达式包裹查询条件，可以在条件之间进行多种操作。与/或|非~等，从而实现一些复杂的查询操作。
    获取价格大于100，并且图书名字中不包含”传“字的图书：
       `Book.objects.filter(Q(price__gte=100)&~Q(name__icontains="传"))`
    

    
## QuerySet.API
  - all 所有
  - filter 过滤
  - exclude 去除
  - get
  - update 更新
  - order_by :会把前面排序的规则给打乱，而使用后面的排序方式
      `Article.objects.order_by("create_time").order_by("author__name")`
    他会根据作者的名字进行排序，而不是使用文章的创建时间。
  - values 显示需要的字段,返回QuerySet对象,但装的是dict
	``` 
	Book.objects.values('id','name') 
	>>> {"id":"XX","name":"xx"}    
	```
  - values_list 显示需要的字段,返回QuerySet对象,但装的是tuple
  	``` 
	Book.objects.values('id','name') 
	>>> ("id":"XX","name":"xx")    
	```
  - selectz_related
  - prefetch_related
