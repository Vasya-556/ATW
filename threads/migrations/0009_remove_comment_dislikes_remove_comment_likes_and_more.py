# Generated by Django 4.2.3 on 2023-08-01 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0008_comment_dislikes_comment_likes_thread_dislikes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='likes',
        ),
        migrations.DeleteModel(
            name='UserRating',
        ),
    ]
