from django.urls import path
from . import views
from student import views as student_view

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('instructor/', views.instructor, name='instructor'),
    # path('student/', views.student, name='student'),
]