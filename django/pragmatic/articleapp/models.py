from django.db import models
from django.contrib.auth.models import User
from projectapp.models import Project

from articleapp.exif import Exif
from PIL import Image
import base64
import time
import datetime

# Create your models here.
class Article(models.Model):
    writer = models.ForeignKey(User,on_delete=models.SET_NULL, related_name='article',null=True)
    project=models.ForeignKey(Project,on_delete=models.SET_NULL, related_name='article',null=True)
    title = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='article/',null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True,null=True)

    def save(self, *args, **kwargs):
        img_file=self.image
        super().save(*args, **kwargs)
        encode=base64.b64encode(img_file.read()).decode('utf-8')
        image=Image.open(img_file)
        temp_dic=Exif(image)
        new_posts=Images()
        new_posts.article_key=self
        new_posts.file_link = str(img_file).replace(".jpg","")
        new_posts.prompt = temp_dic[3]
        new_posts.negative_prompt = temp_dic[4]
        ts=time.time()
        new_posts.timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        new_posts.steps = temp_dic[6]
        new_posts.sampler = temp_dic[7]
        new_posts.cfg_scale = temp_dic[8]
        new_posts.seed = temp_dic[9]
        new_posts.model_hash = temp_dic[10]
        new_posts.clip_skip = temp_dic[11]
        new_posts.denoising_strength = temp_dic[12]
        new_posts.img = encode
        new_posts.save()
        return 0
    
    def delete(self, *args, **kwargs):
        #self.image.delete()
        return super().delete(*args, **kwargs)
    
class Images(models.Model):
    article_key = models.ForeignKey(Article,on_delete=models.SET_NULL, related_name='img',null=True)
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