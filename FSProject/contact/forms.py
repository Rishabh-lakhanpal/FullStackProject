from django import forms
from .models import ContactUs
from django.core.exceptions import ValidationError



class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"

    def clean_fullname(self):
        name = self.cleaned_data['fullname']
        if not name:
            raise ValidationError("Name cannot be empty")
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise ValidationError("Email cannot be empty")
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone:
            raise ValidationError("phone number cannot be empty")
        return phone


    def clean_subject(self):
        subject = self.cleaned_data['subject']
        if not subject:
            raise ValidationError("Subject cannot be empty")
        return subject


    def clean_message(self):
        msg = self.cleaned_data['message']
        if not msg:
            raise ValidationError("Message cannot be empty")
        return msg