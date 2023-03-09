from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.all_programs, name="all-programs"),
    # path('add-program', views.add_program, name="add-program"),
    # path('update-program/<int:id>', views.update_program, name="update-program"),
    # path('delete-program/<int:id>', views.delete_program, name="delete-program"),

]
