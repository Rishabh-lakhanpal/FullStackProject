# Generated by Django 4.1.7 on 2023-02-23 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_created=True, blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_created=True, blank=True, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='complaints')),
                ('status', models.CharField(blank=True, default='Open', max_length=20, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='complains_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='complains_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
