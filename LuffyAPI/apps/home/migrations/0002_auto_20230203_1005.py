# Generated by Django 3.2.16 on 2023-02-03 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='create_time',
            new_name='created_time',
        ),
        migrations.RenameField(
            model_name='banner',
            old_name='last_update_time',
            new_name='updated_time',
        ),
    ]
