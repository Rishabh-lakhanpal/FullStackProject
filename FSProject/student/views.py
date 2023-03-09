
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .forms import StudentDetailForm
from .models import StudentDetail
from django.views import View
from django.contrib.auth.decorators import login_required

# from .decorators import unauthenticated_user
# Create your views here.

# @unauthenticated_user
# @login_required(login_url='login')
def studentlist(request):
    stud = StudentDetail.objects.all()
    context = {
        'stud' : stud
    }
    return render(request, 'student/student_list.html', context)

class HomeViews(View):
    def get(self, request):
        form = StudentDetailForm()
        return render(request, 'student/Student_detail.html', {'form':form})
    
    def post(self, request):
        form = StudentDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Employee added Successfully')
        else:
            print(form.errors)
            return HttpResponse('error')
            # return render(request, 'app/home.html', {'form':'form'})


def updatestudent(request, id):
    if request.method == 'POST':
        stud = StudentDetail.objects.get(pk=id)
        form = StudentDetailForm(request.POST, instance=stud)
        if form.is_valid():
            form.save()
        
    else:
        stud = StudentDetail.objects.get(pk=id)
        form = StudentDetailForm(instance=stud)
    return render(request, 'student/student_update.html',{'form':form})


def delete_data(request, id):
    if request.method == 'POST':
        pi = StudentDetail.objects.get(pk=id)
        pi.delete()
        stud = StudentDetail.objects.all()
        context = {
            'stud' : stud
        }
        return render(request, 'student/student_list.html',context)