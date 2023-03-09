from django.db import models
from django.contrib.auth.models import User



class Complaint(models.Model):
    STATUS = (
        ("Open", "Open"),
        ("In-Process", "In-Process"),
        ("Closed", "Closed")
    )
    title = models.CharField(max_length=200, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    attachment = models.FileField(upload_to="complaints", null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True, default='Open')
    created_date = models.DateTimeField(auto_created=True, null=True, blank=True)
    updated_date = models.DateTimeField(auto_created=True, null=True, blank=True)
    created_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        related_name="complains_created_by")
    updated_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        related_name="complains_updated_by")
