# Generated by Django 3.2.16 on 2023-01-30 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_update_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('orders', models.IntegerField(verbose_name='优先级')),
                ('name', models.CharField(blank=True, max_length=32, null=True, verbose_name='图片名称')),
                ('image', models.ImageField(upload_to='static/banner/', verbose_name='图片')),
                ('link', models.CharField(max_length=64, verbose_name='链接')),
                ('introduction', models.TextField(blank=True, null=True, verbose_name='详情介绍')),
            ],
            options={
                'verbose_name': '轮播表',
                'verbose_name_plural': '轮播表',
                'db_table': 'luffy_banner',
            },
        ),
    ]
