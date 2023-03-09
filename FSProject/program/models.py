from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# from ckeditor.fields import RichTextField



class ToolsCovered(models.Model):
    tool_name = models.CharField(max_length=50, null=True, blank=False)
    tools = models.ImageField(upload_to='tools_covered', default='course-thumbnail.png')

    def __str__(self):
        return self.tool_name

class Program(models.Model):
    STATUS = (
        ("active", "Active"),
        ("inactive", "Inactive")
    )

    LEVEL = (
        ("beginner", "Beginner"),
        ("advanced", "Advanced"),
        ("intermediate", "Intermediate")
    )

    PROGRAM_TYPE = (
        ("public", "Public"),   
        ("regular", "Regular")
    )

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    program_name = models.CharField(max_length=200, null=True, blank=False)
    slug = models.SlugField(max_length = 250, null = True, blank = True, unique=True)
    brief_description = RichTextUploadingField(blank=False, null=True)
    detail_overview = RichTextUploadingField(blank=False, null=True)
    cover_image = models.ImageField(upload_to='course_thumbnail')
    banner_image = models.ImageField(upload_to="course_banner")
    program_level = models.CharField(max_length=30, null=True, blank=False, choices=LEVEL)
    status = models.CharField(max_length=50, choices=STATUS)
    program_start_date = models.DateField(null=True, blank=False)
    program_end_date = models.DateField(null=True, blank=False)
    seats = models.IntegerField(null=True, blank=False)
    tools_covered = models.ManyToManyField(ToolsCovered)
    price = models.FloatField(null=True, blank=True, default=0)
    is_free = models.IntegerField(default=0, null=True, blank=True)
    is_discounted = models.IntegerField(default=0, null=True, blank=True)
    discount_price = models.FloatField(null=True, blank=True)
    meta_keywords = models.TextField(null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    program_type = models.CharField(max_length=25, null=True, blank=False, choices=PROGRAM_TYPE)
    program_duration = models.IntegerField(default=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_subscribed = models.IntegerField(default=0, null=True, blank=True)



    def __str__(self):
        return self.program_name

    # def get_absolute_url(self):
    #     kwargs = {
    #         'slug': self.category_id,
    #         'slug': self.slug
    #     }
    #     return reverse('update-program', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.program_name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class ProgramSchedule(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)


class KeyFeature(models.Model):
    program_id = models.ForeignKey(Program, on_delete=models.CASCADE)
    features = models.CharField(max_length=255)

    def __str__(self):
        return self.features


class SkillsCovered(models.Model):
    program_id = models.ForeignKey(Program, on_delete=models.CASCADE)
    skills = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.skills


class Requirement(models.Model):
    program_id = models.ForeignKey(Program, on_delete=models.CASCADE)
    requirements = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.requirements


class Eligibility(models.Model):
    program_id = models.ForeignKey(Program, on_delete=models.CASCADE)
    eligibility = models.CharField(max_length=300, null=True, blank=False)

    def __str__(self):
        return self.eligibility



class ProgramSection(models.Model):
    program_id = models.ForeignKey(Program, on_delete=models.CASCADE)
    section_title = models.CharField(max_length=500, null=True, blank=False)

    def __str__(self):
        return self.section_title


class ProgramLession(models.Model):
    VIDEO_TYPE = (
        ("video", "Video"),
        ("document", "Document")
    )
    section_id = models.ForeignKey(ProgramSection, on_delete=models.CASCADE)
    lession_title = models.CharField(max_length=300, null=True, blank=False)
    duration = models.CharField(max_length=50, null=True, blank=True)
    lession_type = models.CharField(max_length=30, choices=VIDEO_TYPE, null=True, blank=False)
    video_url = models.FileField(upload_to='lession', null=True, blank=False)
    summary = models.TextField(null=True, blank=False)

    def __str__(self):
        return self.lession_title


class ProgramSkill(models.Model):
    STATUS = (
        ("active", "Active"),
        ("inactive", "Inactive")
    )

    skill = models.CharField(max_length=255, null=True, blank=False)
    status = models.CharField(max_length=20, null=True, blank=False)

    def __str__(self):
        return self.skill


class ProgramComplitionStatus(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    videos = models.TextField(null=True, blank=True)
    video_count = models.IntegerField(default=0, null=True, blank=True)

