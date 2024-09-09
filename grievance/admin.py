from django.contrib import admin
from .models import Grievance, UserGrievance

@admin.register(Grievance)
class GrievanceAdmin(admin.ModelAdmin):
    list_display = ('title', 'urgency', 'created_at')  # Fields to show in list view
    search_fields = ('title', 'description')  # Add search functionality
    list_filter = ('urgency', 'created_at')  # Add filters for urgency and date

@admin.register(UserGrievance)
class UserGrievanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'grievance', 'saved_at')  # Customize list view
    search_fields = ('user__username', 'grievance__title')  # Add search functionality
    list_filter = ('saved_at',)  # Add filter for saved date
