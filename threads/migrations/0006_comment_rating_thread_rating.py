# Generated by Django 4.2.3 on 2023-07-30 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0005_remove_comment_rating_remove_thread_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='thread',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]