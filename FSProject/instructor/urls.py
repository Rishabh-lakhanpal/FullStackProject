from django.urls import path
from . import views



urlpatterns = [
    path('instructor-registration', views.instructorRegistration, name="instructor-registration"),
    path('instructor-list', views.instructor_view, name="instructor-list"),
    # path('update-instructor/<int:id>', views.updateInstructor, name="update-instructor"),
    path('instructor-detail/<int:id>', views.instructor_detail, name="instructor-detail"),
]
