from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ComplaintForm
from . import models
from django.contrib.auth.models import User
from complaint.models import Complaint
from datetime import datetime


def complains(request):
    context = {
        "title": "Complaints",
        "complains": models.Complaint.objects.all(),
        "mesages": models.Complaint.objects.all().order_by('-id')[:5]
    }
    return render(request, 'complaint/complains.html', context)


def complainsResponse(request, ref_id):
    try:
        complaint = models.Complaint.objects.get(id=ref_id)

        context = {
            "title": "Complaint Response",
            "complaint": complaint,
            "mesages": models.Complaint.objects.all().order_by('-id')[:5]
    
        }
        return render(request, 'complaint/complains-response.html', context)

    except Exception as e:
        messages.error(request, str(e))
        return redirect('complaint') 
    


'''
    Desc: Add Complaint
    Date: 23-02-2022
'''

@login_required
def addComplaint(request):
    if request.method == "POST":
        try:
            complaintForm = ComplaintForm(request.POST, request.FILES)
            if complaintForm.is_valid():
                form = complaintForm.save(commit=False)
                form.status = "Open"
                form.created_by = request.user
                form.created_date = datetime.now()
                form.save()

                messages.success(request, "Complaint added")
                return redirect('complaint')
            else:
                messages.error(request, "Please enter valid data")
                return redirect('complaint')
        except Exception as e:
            messages.error(request, str(e))
            return redirect('complaint')  
    

    context = {
        "title": "Add Complaint",
        "mesages": models.Complaint.objects.all().order_by('-id')[:5]
    }
    

    return render(request, 'complaint/add-complaint.html', context)



@login_required
def deleteComplain(request, ref_id):
    try:
        complain = models.Complaint.objects.get(id=ref_id)
        complain.delete()
        messages.success(request, "Complaint deleted successfully.")
        return redirect('complaint')
    except Exception as e:
        messages.error(request, str(e))
        return redirect('complaint')



@login_required
def processComplain(request, ref_id):
    try:
        complain = models.Complaint.objects.get(id=ref_id)
        complain.status = "In-Process"
        complain.save()
        messages.success(request, "Complaint marked in-process successfully.")
        return redirect('complaint')
    except Exception as e:
        messages.error(request, str(e))
        return redirect('complaint')        



@login_required

def closeComplain(request, ref_id):
    try:
        complain = models.Complaint.objects.get(id=ref_id)
        complain.status = "Closed"
        complain.updated_date = datetime.now()
        complain.updated_by = request.user
        complain.save()
        messages.success(request, "Complaint marked closed successfully.")
        return redirect('complaint')
    except Exception as e:
        messages.error(request, str(e))
        return redirect('complaint')        



@login_required
def reopenComplain(request, ref_id):
    try:
        complain = models.Complaint.objects.get(id=ref_id)
        complain.status = "Open"
        complain.created_date = datetime.now()
        complain.created_by = request.user
        complain.updated_date = None
        complain.save()
        messages.success(request, "Complaint re-open successfully.")
        return redirect('complaint')
    except Exception as e:
        messages.error(request, str(e))
        return redirect('complaint')    