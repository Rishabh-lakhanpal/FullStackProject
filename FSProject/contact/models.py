from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class ContactUs(models.Model):
    fullname = models.CharField(max_length=200, null=True, blank=True)
    email    = models.EmailField(null=True, blank=True)
    phone    = models.CharField(max_length=20, null=True, blank=True)
    subject  = models.CharField(max_length=255, null=True, blank=True)
    message  = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname
    

class WebsiteSetting(models.Model):
    black_logo = models.ImageField(upload_to="logos", null=True, blank=False)
    white_logo = models.ImageField(upload_to="logos", null=True, blank=False)
    # website_banner = models.ImageField(upload_to="website_banner", null=True, blank=False)
    support_contact = models.CharField(max_length=20, null=True, blank=False)
    location = models.CharField(max_length=100, null=True, blank=False)
    support_email = models.EmailField(null=True, blank=False)
    address = models.TextField(null=True, blank=False)
    contact_no = models.CharField(max_length=30, null=True, blank=False)
    contact_email = models.EmailField(null=True, blank=False)
    facebook = models.CharField(max_length=200, null=True, blank=False)
    twitter = models.CharField(max_length=200, null=True, blank=False)
    instagram = models.CharField(max_length=200, null=True, blank=False)
    linkedin = models.CharField(max_length=200, null=True, blank=False)
    pinterest = models.CharField(max_length=200, null=True, blank=False)
    slug = models.SlugField(max_length=250, null=True, blank=True)


    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse("website-settings", kwargs={"slug":self.slug})
