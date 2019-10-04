from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.models import ContentType
from read_record.models import readNumMethod

# 博客分类
class BlogType(models.Model):
    typeName=models.CharField(max_length=8)

    def __str__(self):
        return self.typeName

# 博客基本信息
class Blog(models.Model,readNumMethod):
    blogTitle=models.CharField(max_length=30)
    blogContent=RichTextUploadingField()
    blogAuthor=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    blog_createdTime=models.DateTimeField(auto_now_add=True)
    blog_updatedTime=models.DateTimeField(auto_now=True)
    blogType=models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)
    blog_img=models.ImageField(upload_to="blogImage",default='blogImage/default.jpg')

    def __str__(self):
        return "<Blog:%s>"%self.blogTitle

    class Meta:
        ordering=['-blog_createdTime']

