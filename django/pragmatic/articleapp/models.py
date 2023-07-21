from django.db import models
from django.contrib.auth.models import User
from projectapp.models import Project



# Create your models here.
class Article(models.Model):
    writer = models.ForeignKey(User,on_delete=models.SET_NULL, related_name='article',null=True)
    project=models.ForeignKey(Project,on_delete=models.SET_NULL, related_name='article',null=True)
    title = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='article/',null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True,null=True)

    def delete(self, *args, **kwargs):
        self.image.delete()
        return super().delete(*args, **kwargs)
    
class Images(models.Model):
    article_key = models.ForeignKey(Article,on_delete=models.SET_NULL, related_name='img',null=True)
    user = models.CharField(primary_key=True, max_length=40)
    name = models.CharField(max_length=255, blank=True, null=True)
    file_link = models.CharField(max_length=255, blank=True, null=True)
    prompt = models.TextField(blank=True, null=True)
    negative_prompt = models.TextField(blank=True, null=True)
    timestamp = models.CharField(max_length=20, blank=True, null=True)
    steps = models.IntegerField(blank=True, null=True)
    sampler = models.CharField(max_length=50, blank=True, null=True)
    cfg_scale = models.IntegerField(blank=True, null=True)
    seed = models.CharField(max_length=10, blank=True, null=True)
    model_hash = models.CharField(max_length=20, blank=True, null=True)
    clip_skip = models.IntegerField(blank=True, null=True)
    denoising_strength = models.CharField(max_length=10, blank=True, null=True)
    img = models.TextField(blank=True, null=True)