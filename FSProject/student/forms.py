from django import forms
from .models import StudentDetail

GENDER_CHOICE = [
    ('Male', 'Male'),
    ('Female', "Female")
]


class StudentDetailForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICE, widget=forms.RadioSelect)
    class Meta:
        model = StudentDetail
        fields = ['id', 'name', 'dob','mobile','email', 'gender', 'locality',
        'city', 'pin', 'state', 'profile_image']
        labels = {'name':'Full Name', 'dob':'Date of Birth',
        'pin':'Pin Code', 'mobile':'Mobile No.', 'email':'Email Id',
        'profile_image':'Profile Image'}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            # 'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }