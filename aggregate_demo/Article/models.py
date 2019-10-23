from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=8)
    age = models.IntegerField()

    class Meta:
        db_table = 'author'

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'publisher'

    def __str__(self):
        return self.name



class Book(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    rate = models.FloatField()
    pages = models.IntegerField()
    author = models.ForeignKey('Author',on_delete=models.CASCADE)
    publisher = models.ForeignKey('Publisher',on_delete=models.CASCADE)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.name


class Sales(models.Model):
    name = models.ForeignKey('Book',on_delete=models.CharField)
    price = models.FloatField()
    num = models.IntegerField(default=0)
    end_time = models.DateField(auto_now_add=True)


    class Meta:
        db_table = 'sales'
