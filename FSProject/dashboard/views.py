from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login_view')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

@login_required(login_url='login_view')
def profile(request):
    return render(request, 'dashboard/profile.html')