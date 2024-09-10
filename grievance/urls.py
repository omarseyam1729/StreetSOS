from django.urls import path
from .views import GrievanceListView, GrievanceCreateView, GrievanceDetailView, save_grievance, SavedGrievancesListView
from .views import delete_grievance

urlpatterns = [
    path('', GrievanceListView.as_view(), name='grievance-list'),
    path('new/', GrievanceCreateView.as_view(), name='grievance-create'),
    path('save/<int:grievance_id>/', save_grievance, name='save-grievance'),
    path('saved/', SavedGrievancesListView.as_view(), name='saved-grievances'),
    path('grievance/<int:pk>/', GrievanceDetailView.as_view(), name='grievance-detail'),
    path('delete/<int:grievance_id>/', delete_grievance, name='delete-grievance'),
]
