# Generated by Django 4.1.10 on 2023-07-21 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0006_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='name',
        ),
    ]
