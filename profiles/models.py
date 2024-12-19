from django.db import models
from users.models import CustomUser    # Ensure this imports your CustomUser  model

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #user = models.OneToOneField(CustomUser , on_delete=models.CASCADE)  # Link to CustomUser 
    bio = models.TextField(blank=True)  # Short biography
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)  # Profile picture
    location = models.CharField(max_length=100, blank=True)  # User's location
    birth_date = models.DateField(null=True, blank=True)  # User's birth date

    def __str__(self):
        return self.user.username