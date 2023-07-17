from django.db import models

# Create your models here.
class CivitTest(models.Model):
    user_id = models.CharField(primary_key=True, max_length=10)
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

    class Meta:
        managed = False
        db_table = 'civit_test'