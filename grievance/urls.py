from django.urls import path
from .views import GrievanceListView, GrievanceCreateView, save_grievance

urlpatterns = [
    path('', GrievanceListView.as_view(), name='grievance-list'),
    path('create/', GrievanceCreateView.as_view(), name='grievance-create'),
    path('save/<int:grievance_id>/', save_grievance, name='grievance-save'),
]
