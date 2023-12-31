# Generated by Django 4.2.3 on 2023-07-26 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Comment_text')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
            ],
            options={
                'ordering': ['time_create'],
            },
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Time of publication')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Time of update')),
                ('full_text', models.TextField(verbose_name='Full text')),
            ],
            options={
                'ordering': ['time_create', 'title'],
            },
        ),
    ]
