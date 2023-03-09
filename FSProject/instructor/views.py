from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from .models import InstructorPreviousWorkExperience
from .forms import InstructorProfileForm, InstructorPreviousExperienceForm, UserRegistrationForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.core.serializers import serialize


def instructorRegistration(request):
    if request.method == "POST":

        instructor_form = UserRegistrationForm(request.POST)
        instructor_profile = InstructorProfileForm(request.POST, request.FILES)
        experience_form = InstructorPreviousExperienceForm(request.POST)

        if instructor_form.is_valid() and instructor_profile.is_valid() and experience_form.is_valid():
            user = instructor_form.save()

            group = Group.objects.get(name="instructor")
            user.groups.add(group)

            instructor_profile.save()
            expr = experience_form.save(commit=False)
            expr.instructor = user
            expr.save()
            messages.success(request, "Instructor added successfully!")
            return redirect('instructor-list')
        else:
            print(instructor_form.errors)
            print(instructor_profile.errors)
            print(experience_form.errors)
            uname = User.objects.filter(username=request.POST.get('username')).first()
            uemail = User.objects.filter(email=request.POST.get('email')).first()

            if uname:
                messages.error(request, "Username is already exists.")
            elif uemail:
                messages.error(request, "Email is already exists.")
            elif len(request.POST.get('password1'))<8:
                messages.error(request, "Password should be alphanumeric & should contain 8 characters.")
            else:    
                messages.error(request, "Error..Try again!")
            return redirect('instructor-registration')
    else:
        instructor_form = UserRegistrationForm()
        instructor_profile = InstructorProfileForm()
        experience_form = InstructorPreviousExperienceForm()
        context = {
            'instructor_form': instructor_form,
            'instructor_profile': instructor_profile,
            'experience_form': experience_form,
        }

        return render(request, 'instructor/instructor-registration.html', context=context)


def instructor_view(request):
    data = InstructorPreviousWorkExperience.objects.all()
    instructor_form = UserRegistrationForm()
    instructor_profile = InstructorProfileForm()
    experience_form = InstructorPreviousExperienceForm()

    context = {
        'instructors': data,
        'instructor_form': instructor_form,
        'instructor_profile': instructor_profile,
        'experience_form': experience_form,
        }
    return render(request, 'instructor/instructor-list.html', context)


def instructor_detail(request,id):
    instructor = User.objects.get(id=id)
    # profile = Profile.objects.get(user=instructor.id)
    experience = InstructorPreviousWorkExperience.objects.get(instructor=instructor.id)

    context = {
        'instructor': instructor,
        # 'profile': profile,
        'experience': experience,
        }
    return render(request, 'instructor/instructor-detail.html', context)


# def updateInstructor(request, id):
#     instructor = User.objects.get(id=id)

#     experience = InstructorPreviousWorkExperience.objects.filter(instructor=instructor.id).first()
#     if request.method == "POST":
#         print(request.POST)
#         instructor_form = UserRegistrationForm(request.POST, instance=instructor)
#         instructor_profile = InstructorProfileForm(request.POST, request.FILES, instance=instructor.profile)
#         if instructor_form.is_valid():
#             instructor = instructor_form.save()
#             prof = instructor_profile.save(commit=False)
#             # print(prof)
#             prof.user = instructor
#             prof.save()

#             InstructorPreviousWorkExperience.objects.filter(instructor=instructor.id).delete()

#             institute_name = request.POST.getlist('institute_name')
#             period_of_working = request.POST.getlist('period_of_working')
#             experience_in = request.POST.getlist('experience_in')

#             for inst, wrk_exp, exp in zip(institute_name, period_of_working, experience_in):
#                 if inst and wrk_exp and exp:
#                     InstructorPreviousWorkExperience.objects.create(instructor=instructor, institute_name=inst, period_of_working=wrk_exp, experience_in=exp)

#             # expr = experience_form.save(commit=False)
#             # expr.instructor = instructor
#             # expr.save()
#             messages.success(request, "Instructor updated successfully!")
#             return redirect('instructor-list')
#         else:
#             print(instructor_form.errors(), instructor_profile.errors())
#             messages.error(request, "Error..try again!")
#             return redirect('instructor-list')


#     else:
#         previous_exp = InstructorPreviousWorkExperience.objects.filter(instructor=id)
#         instructor_form = UserRegistrationForm(instance=instructor)
#         instructor_profile = InstructorProfileForm(instance=instructor.instructor)
#         experience_form = InstructorPreviousExperienceForm(instance=experience)
#         print(previous_exp)

#         context = {
#             'instructor_form': instructor_form,
#             'instructor_profile': instructor_profile,
#             'experience_form': experience_form,
#             'id':id,
#             'previous_exp':previous_exp,
#         }

#         return render(request, 'instructor/instructor-update.html', context=context)





