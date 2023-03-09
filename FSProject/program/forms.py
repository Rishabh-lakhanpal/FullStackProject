from django import forms
from . import models
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.core.exceptions import ValidationError



class ProgramFrom(forms.ModelForm):
    meta_keywords = forms.CharField(widget=forms.Textarea(
        attrs={
            "cols": 5,
            "rows": 3
        }
    ))
    meta_description = forms.CharField(widget=forms.Textarea(
        attrs={
            "cols": 5,
            "rows": 3
        }
    ))
    program_start_date = forms.DateField(required=False, widget=forms.DateInput(
        attrs={
            'type': "date"
        }
    ))
    program_end_date = forms.DateField(required=False, widget=forms.DateInput(
        attrs={
            'type': "date"
        }
    ))

    class Meta:
        model = models.Program
        fields = ['program_name', 'brief_description', 'detail_overview', 'cover_image', 'banner_image', 'program_level',
            'status', 'program_start_date', 'program_end_date', 'seats','tools_covered',
           'price', 'is_free', 'is_discounted', 'discount_price', 'meta_keywords', 'meta_description', 'program_type',
           'program_duration', 'is_subscribed']

    def __init__(self, *args, **kwargs):
        super(ProgramFrom, self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = "Select Status"
        self.fields['program_type'].empty_label = "Select Program Type"

    def clean(self):
        cleaned_data = super(ProgramFrom, self).clean()
        name = cleaned_data.get('program_name')
        des = cleaned_data.get('brief_description')
        seat = cleaned_data.get('seats')
        tool = cleaned_data.get('tools_covered')
        duration = cleaned_data.get('program_duration')
        type = cleaned_data.get('program_type')
        if not name and not des and not seat and not tool and not duration and not type:
            raise forms.ValidationError("You have left some empty box, Please fill the data")


class ProgramScheduleForm(forms.ModelForm):
    start_date = forms.DateField(required=False, widget=forms.DateInput(
        attrs={
            'type': "date"
        }
    ))
    end_date = forms.DateField(required=False, widget=forms.DateInput(
        attrs={
            'type': "date"
        }
    ))
    class Meta:
        model = models.ProgramSchedule
        fields = "__all__"



class KeyFeaturesForm(forms.ModelForm):
    class Meta:
        model = models.KeyFeature
        fields = ['features']

    def clean_features(self):
        feat = self.cleaned_data.get('features')
        if not feat:
            raise forms.ValidationError("Features cannot be empty")
        return feat

class SkillsCoveredForm(forms.ModelForm):
    class Meta:
        model = models.SkillsCovered
        fields = ['skills']

    def clean_skills(self):
        skill = self.cleaned_data.get('skills')
        if not skill:
            raise forms.ValidationError("skills cannot be empty")
        return skill



class ToolsCoveredForm(forms.ModelForm):
    class Meta:
        model = models.ToolsCovered
        fields = '__all__'
        exclude = ('program_id',)

    def clean_tool_name(self):
        tool = self.cleaned_data.get('tool_name')
        if not tool:
            raise forms.ValidationError("Tool name cannot be empty")
        return tool


class RequirementForm(forms.ModelForm):
    class Meta:
        model = models.Requirement
        fields = ['requirements']

    def clean_requirements(self):
        req = self.cleaned_data.get('requirements')
        if not req:
            raise forms.ValidationError("Requirements cannot be empty")
        return req


class ProgramSectionForm(forms.ModelForm):
    class Meta:
        model = models.ProgramSection
        fields = ['section_title']

    def clean_section_title(self):
        section = self.cleaned_data.get('section')
        if not section:
            raise forms.ValidationError("Section title cannot be empty")
        return section


class ProgramLessionForm(forms.ModelForm):
    class Meta:
        model = models.ProgramLession
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(ProgramLessionForm, self).__init__(*args, **kwargs)
        self.fields['section_id'].label = "Select Section"


    def clean(self):
        cleaned_data = super(ProgramLessionForm, self).clean()
        lession = cleaned_data.get('lession_title')
        type = cleaned_data.get('lession_type')
        if not lession and not type:
            raise forms.ValidationError("Lession Title and Type cannot be empty")



class ProgramSkillForm(forms.ModelForm):
    class Meta:
        model = models.ProgramSkill
        fields = "__all__"

    def clean_skill(self):
        skill = self.cleaned_data.get('skill')
        if not skill:
            raise forms.ValidationError("Skills cannot be empty")
        return skill

