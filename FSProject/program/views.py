from django.shortcuts import render, redirect, get_object_or_404

from .models import (
                Program, 
                ToolsCovered, 
                KeyFeature, 
                SkillsCovered, 
                ProgramSection, 
                ProgramLession, 
                Eligibility, 
                Requirement,
                ProgramSkill,
                ProgramSchedule
            )
from . import forms
from .forms import KeyFeaturesForm,ProgramSkillForm,RequirementForm,SkillsCoveredForm,ToolsCoveredForm
from django.contrib import messages
from django.core.serializers import serialize
from django.http import JsonResponse
from django.http import HttpResponse
from django.core.serializers import serialize
from django.http import JsonResponse



def all_programs(request):
    programs = Program.objects.all()
    free_program = Program.objects.filter(is_free=1).count()
    paid_program = Program.objects.filter(is_free=0).count()

    if request.user.groups.all()[0].name == "instructor":
        programs = Program.objects.filter(created_by=request.user)
        free_program = Program.objects.filter(created_by=request.user, is_free=1).count()
        paid_program = Program.objects.filter(created_by=request.user, is_free=0).count()

    context = {
         "programs": programs, 
         "free_program": free_program,
         "paid_program": paid_program,
        }

    return render(request, "program/all_programs.html", context=context)

