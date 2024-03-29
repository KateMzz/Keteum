# Generated by Django 4.1.7 on 2023-04-12 13:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0014_alter_post_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_likes',
            field=models.ManyToManyField(blank=True, default=None, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
