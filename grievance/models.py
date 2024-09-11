from django.db import models
from users.models import UserProfile  # Import the UserProfile model

class Grievance(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='grievances')
    title = models.CharField(max_length=255)
    description = models.TextField()
    urgency = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Urgency from 1 to 5
    latitude = models.DecimalField(max_digits=40, decimal_places=14)
    longitude = models.DecimalField(max_digits=40, decimal_places=14)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} (Urgency: {self.urgency})"

class UserGrievance(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # Link to UserProfile
    grievance = models.ForeignKey(Grievance, on_delete=models.CASCADE)  # Link to Grievance
    saved_at = models.DateTimeField(auto_now_add=True)  # When was the grievance saved

    class Meta:
        unique_together = ('user', 'grievance')  # Prevents the same user from saving the same grievance multiple times

    def __str__(self):
        return f"{self.user.user.username} saved {self.grievance.title}"  # Access the username from the related User object
