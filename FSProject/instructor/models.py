from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Instructor(models.Model):
    user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=20, null=True, blank=True)
    short_description = models.TextField(max_length=255, null=True, blank=True)
    profile_image = models.ImageField(default="default.png", upload_to="profile_img", null=True, blank=True)
    qualification = models.CharField(max_length=200, null=True, blank=True)
    exprience = models.CharField(max_length=10, null=True, blank=True)
    expertise = models.CharField(max_length=255, null=True, blank=True)


class InstructorPreviousWorkExperience(models.Model):
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    institute_name = models.CharField(max_length=255, null=True, blank=True)
    period_of_working = models.CharField(max_length=100, null=True, blank=True)
    experience_in = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.instructor.first_name


class Instructor_messages(models.Model):
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(max_length=350, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.instructor.first_name
