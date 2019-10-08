# Generated by Django 2.2.5 on 2019-10-08 02:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20191006_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='chewning.cl@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='vote',
            field=models.ManyToManyField(blank=True, related_name='vote', to=settings.AUTH_USER_MODEL),
        ),
    ]