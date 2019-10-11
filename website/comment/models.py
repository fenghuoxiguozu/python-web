from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Comment(models.Model):
    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField()
    content_object=GenericForeignKey('content_type','object_id')

    commentText=models.TextField()
    commentTime=models.DateTimeField(auto_now_add=True)
    commentUser=models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")

    # 回复模型，外键关联自己
    root=models.ForeignKey('self',null=True,on_delete=models.CASCADE,related_name="root_comment")
    parent= models.ForeignKey('self',null=True,on_delete=models.CASCADE,related_name="parent_comment")
    reply_to=models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name="replies")

    def __str__(self):
        return self.commentText

    class Meta:
        ordering=['-commentTime']

