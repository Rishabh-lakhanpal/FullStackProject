# Generated by Django 4.1.7 on 2023-02-22 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='twitter',
        ),
    ]