from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'karma', 'bio')  # Customize the columns displayed in the list view
    search_fields = ('user__username', 'user__email', 'bio')  # Add search functionality for username, email, and bio
    list_filter = ('karma',)  # Add filter by karma to the right-hand side
    ordering = ('-karma',)  # Default order by karma, descending

    # Optional: Customize the display in the form view
    fieldsets = (
        (None, {
            'fields': ('user', 'bio', 'profile_picture', 'karma'),
        }),
    )

    # Optional: Add a method to display profile pictures in the list view
    def profile_picture_tag(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.profile_picture.url))
        return "-"
    profile_picture_tag.short_description = 'Profile Picture'
