from django.urls import path
from users.views import UserProfileDetailView, UserProfileUpdateView, CustomLoginView, register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('profile/', UserProfileDetailView.as_view(), name='profile-detail'),
    path('profile/edit/', UserProfileUpdateView.as_view(), name='profile-edit'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='grievance-list'), name='logout'),
    path('register/', register, name='register'),
]
