from django.urls import path
from .views import (
    GrievanceListView, GrievanceCreateView, GrievanceDetailView, 
    save_grievance, SavedGrievancesListView, delete_grievance, MyGrievancesListView
)

urlpatterns = [
    # List all grievances
    path('', GrievanceListView.as_view(), name='grievance-list'),
    
    # Create a new grievance
    path('new/', GrievanceCreateView.as_view(), name='grievance-create'),
    
    # Save a grievance
    path('save/<int:grievance_id>/', save_grievance, name='save-grievance'),
    
    # View saved grievances
    path('saved/', SavedGrievancesListView.as_view(), name='saved-grievances'),
    
    # View grievance details by ID
    path('grievance/<int:pk>/', GrievanceDetailView.as_view(), name='grievance-detail'),
    
    # Delete a grievance by ID
    path('delete/<int:grievance_id>/', delete_grievance, name='delete-grievance'),
    
    # View grievances submitted by the logged-in user
    path('my-grievances/', MyGrievancesListView.as_view(), name='my-grievances'),  # Add My Grievances URL
]
