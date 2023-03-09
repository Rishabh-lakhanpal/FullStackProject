from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.HomeViews.as_view()), name="student-details"),
    path('student-list', views.studentlist, name="student-list"),
    path('update-student/<int:id>', views.updatestudent, name="update-student"),
    path('delete/<int:id>', views.delete_data, name="deletedata"),
]
