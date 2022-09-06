# Generated by Django 4.1 on 2022-09-06 05:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='views',
            field=models.ManyToManyField(related_name='room_views', to=settings.AUTH_USER_MODEL),
        ),
    ]
