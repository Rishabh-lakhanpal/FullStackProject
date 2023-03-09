from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
# from .decorators import unauthenticated_user
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index1.html')

# @unauthenticated_user
def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(id=request.POST.get('group'))
            user.groups.add(group)

            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
        groups = Group.objects.all()
    return render(request,'register.html', {'form': form, 'msg': msg, 'groups': groups})

# @unauthenticated_user
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.groups.all()[0].name == "Admin":
                    return redirect('dashboard')
                elif user.groups.all()[0].name == "Instructor":
                    return redirect('instructor')
                elif user.groups.all()[0].name == "Student":
                    return redirect('student-details')
                else:
                    msg= 'invalid credentials'
            else:
                msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

def logout(request):
    request.session.flush()
    messages.success(request, "Logout successfully.")
    return redirect(index)


@login_required(login_url='login')
def admin(request):
    return render(request,'admin.html')

@login_required(login_url='login')
def instructor(request):
    return render(request,'instructor.html')

@login_required(login_url='login')
def student(request):
    return render(request,'student.html')