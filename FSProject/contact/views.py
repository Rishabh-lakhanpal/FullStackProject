from django.shortcuts import render
from .forms import ContactUsForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .common import getWebSetting
# Create your views here.

def contactUs(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, "Request sent successfully!")
            return redirect('contact-us')
        else:
            messages.error(request, "Error..try again!")
            return redirect('contact-us')
   
    context = {
        "web"         : getWebSetting(),
        # "footer_pages":  getSection(request)
    }
    return render(request, 'contact/contact-us.html', context=context)