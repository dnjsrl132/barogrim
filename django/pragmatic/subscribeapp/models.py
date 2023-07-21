from django.db import models
from django.contrib.auth.models import User
from projectapp.models import Project

# Create your models here.
class Subscription(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='subscription')
    project=models.ForeignKey(Project,on_delete=models.CASCADE, related_name='subscription')
    title = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='article/',null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True,null=True)
    class Meta:
        unique_together = ('user','project')