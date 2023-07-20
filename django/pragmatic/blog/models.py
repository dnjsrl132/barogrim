from django.db import models
from view.models import CivitTest
from django.conf import settings
# Create your models here.
class Post(models.Model):
    #id=models.IntegerField(primary_key=True)
    postname=models.CharField(max_length=50)
    contents = models.TextField()

    def __str__(self):
        return self.postname

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content