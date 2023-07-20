from django.db import models
from django.contrib.auth.models import User
from articleapp.models import Article
# Create your models here.
class Comments(models.Model):
    article = models.ForeignKey(Article,on_delete=models.SET_NULL,null=True, related_name='comments')
    writer = models.ForeignKey(User,on_delete=models.SET_NULL, related_name='comments',null=True)

    content = models.TextField(null=False)

    created_at = models.DateField(auto_now=True,null=True)