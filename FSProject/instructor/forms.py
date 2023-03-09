from django import forms
from .models import Instructor,InstructorPreviousWorkExperience
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "placeholder": "Enter email"
        }
    ))

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Enter username"
        }
    ))

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Enter first name"
        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Enter last name"
        }
    ))

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={
            "placeholder": "Enter password"
        }
    ))

    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(
        attrs={
            "placeholder": "Password confirmation"
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    

    # def clean_username(self):
    #     user = User.objects.filter(username=self.cleaned_data['username'])
    #     if user is not None:
    #         raise forms.ValidationError("Username already in used!")
        
    #     return self.cleaned_data['username']
            

    
    def clean_email(self):
        user = User.objects.filter(email=self.cleaned_data.get('email'))
        if user.exists():
            raise forms.ValidationError("Email already in used!")
        else:
            return self.cleaned_data['email']
                    

    
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1']:
            self.fields[fieldname].help_text = None


class InstructorProfileForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = [
            'profile_image', 
            'contact', 
            'short_description', 
            'qualification', 
            'exprience', 
            'expertise', 
            'linkedin'
        ]

    def clean_contact(self):
        contact = self.cleaned_data['contact']
        if not contact:
            raise ValidationError("Contact cannot be empty")
        return contact

    def clean_qualification(self):
        qualif = self.cleaned_data['qualification']
        if not qualif:
            raise ValidationError("Qualification cannot be empty")
        return qualif

    def clean_exprience(self):
        exp = self.cleaned_data['exprience']
        if not exp:
            raise ValidationError("Experience cannot be empty")
        return exp



class InstructorPreviousExperienceForm(forms.ModelForm):
    class Meta:
        model = InstructorPreviousWorkExperience
        fields = '__all__'


    def clean_institute_name(self):
        institute = self.cleaned_data['institute_name']
        if not institute:
            raise ValidationError("Institute name cannot be empty")
        return institute

    def clean_period_of_working(self):
        period = self.cleaned_data['period_of_working']
        if not period:
            raise ValidationError("working period cannot be empty")
        return period

    def clean_experience_in(self):
        exp = self.cleaned_data['experience_in']
        if not exp:
            raise ValidationError("Experience in cannot be empty")
        return exp
