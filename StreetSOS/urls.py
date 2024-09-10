from django.urls import path
from users.views import UserProfileDetailView, UserProfileUpdateView, CustomLoginView, register
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from grievance.views import GrievanceListView  # Not grievances.views

urlpatterns = [
    path('profile/', UserProfileDetailView.as_view(), name='profile-detail'),
    path('profile/edit/', UserProfileUpdateView.as_view(), name='profile-edit'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('', include('grievance.urls')),
]
