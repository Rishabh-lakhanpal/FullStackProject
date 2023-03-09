from django.urls import path
from . import views


urlpatterns = [
    path('', views.complains, name="complaint"),
    path('complain-reponse/<int:ref_id>', views.complainsResponse, name="complain-reponse"),
    path('add-complaint', views.addComplaint, name="add-complaint"),
    path('delete-complain/<int:ref_id>', views.deleteComplain, name="delete-complain"),
    path('process-complain/<int:ref_id>', views.processComplain, name="process-complain"),
    path('close-complain/<int:ref_id>', views.closeComplain, name="close-complain"),
    path('reopen-complain/<int:ref_id>', views.reopenComplain, name="reopen-complain"),
]