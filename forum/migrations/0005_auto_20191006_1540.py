# Generated by Django 2.2.5 on 2019-10-06 20:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0004_post_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='score',
        ),
        migrations.AddField(
            model_name='post',
            name='vote',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
