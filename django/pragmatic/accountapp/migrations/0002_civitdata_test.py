# Generated by Django 4.1.10 on 2023-07-17 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CivitData',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('file_link', models.CharField(blank=True, max_length=255, null=True)),
                ('prompt', models.TextField(blank=True, null=True)),
                ('negative_prompt', models.TextField(blank=True, null=True)),
                ('timestamp', models.CharField(blank=True, max_length=20, null=True)),
                ('steps', models.IntegerField(blank=True, null=True)),
                ('sampler', models.CharField(blank=True, max_length=50, null=True)),
                ('cfg_scale', models.IntegerField(blank=True, null=True)),
                ('seed', models.CharField(blank=True, max_length=10, null=True)),
                ('model_hash', models.CharField(blank=True, max_length=20, null=True)),
                ('clip_skip', models.IntegerField(blank=True, null=True)),
                ('denoising_strength', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'civit_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('file_link', models.CharField(blank=True, max_length=255, null=True)),
                ('prompt', models.TextField(blank=True, null=True)),
                ('negative_prompt', models.TextField(blank=True, null=True)),
                ('timestamp', models.CharField(blank=True, max_length=20, null=True)),
                ('steps', models.IntegerField(blank=True, null=True)),
                ('sampler', models.CharField(blank=True, max_length=50, null=True)),
                ('cfg_scale', models.IntegerField(blank=True, null=True)),
                ('seed', models.CharField(blank=True, max_length=10, null=True)),
                ('model_hash', models.CharField(blank=True, max_length=20, null=True)),
                ('clip_skip', models.IntegerField(blank=True, null=True)),
                ('denoising_strength', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'test',
                'managed': False,
            },
        ),
    ]
