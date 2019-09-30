from django.db import models
from django.contrib.auth.models import User

# 博客分类
class BlogType(models.Model):
    typeName=models.CharField(max_length=8)

    def __str__(self):
        return self.typeName

# 博客基本信息
class Blog(models.Model):
    blogTitle=models.CharField(max_length=30)
    blogContent=models.TextField()
    blogAuthor=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    blog_createdTime=models.DateTimeField(auto_now_add=True)
    blog_updatedTime=models.DateTimeField(auto_now=True)
    blogType=models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)

    def __str__(self):
        return "<Blog:%s>"%self.blogTitle

    class Meta:
        ordering=['-blog_createdTime']

