from django.contrib import admin
from .models import Instructor, InstructorPreviousWorkExperience, Instructor_messages


admin.site.register(InstructorPreviousWorkExperience)
admin.site.register(Instructor)
admin.site.register(Instructor_messages)
