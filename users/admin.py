
# Register your models here.
from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)  # Decorator to register the model
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'karma')  # Customize the list view in admin
    search_fields = ('user__username', 'bio')  # Add search functionality
