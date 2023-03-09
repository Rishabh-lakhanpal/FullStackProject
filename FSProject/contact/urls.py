from django.urls import path
from . import views

urlpatterns = [
    path('contact-us', views.contactUs, name="contact-us"),
]

