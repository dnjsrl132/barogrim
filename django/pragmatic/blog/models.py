from django.db import models
from view.models import CivitTest

# Create your models here.
class Post(models.Model):
    #id=models.IntegerField(primary_key=True)
    postname=models.CharField(max_length=50)
    contents = models.TextField()

    def __str__(self):
        return self.postname

