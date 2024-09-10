from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Include the users app URLs
    path('', include('grievance.urls')),    # Include the grievance app URLs
]