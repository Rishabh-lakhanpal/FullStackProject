# Generated by Django 4.1.7 on 2023-02-21 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdetail',
            name='job_city',
        ),
        migrations.RemoveField(
            model_name='studentdetail',
            name='my_file',
        ),
    ]
