from django.db import models
from django.contrib.auth.models import User

from properties import settings


class Property(models.Model):
    title = models.CharField(max_length=100)  # Title of the property
    description = models.TextField()  # Description of the property
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the property
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for property creation

    class Meta:
        verbose_name = "Property"  # Singular name for the model
        verbose_name_plural = "Properties"  # Plural name for the model

class Inquiry(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)  # Foreign key to the Property model
    user_email = models.EmailField()  # Email of the user making the inquiry
    message = models.TextField()  # Message content of the inquiry
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for inquiry creation

    class Meta:
        verbose_name = "Inquiry"  # Singular name for the model
        verbose_name_plural = "Inquiries"  # Plural name for the model
        unique_together = (("property", "user_email"),)  # Ensure unique inquiry per property and email

class DashboardActivity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)  # Type of activity performed
    activity_date = models.DateTimeField(auto_now_add=True)  # Timestamp for activity date

    class Meta:
        verbose_name = "Dashboard Activity"  # Singular name for the model
        verbose_name_plural = "Dashboard Activity"  # Plural name for the model

    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"

class UserProfile(models.Model):
    user = models.OneToOneField('settings.AUTH_USER_MODEL', on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/')

    def __str__(self):
        return self.user.username
