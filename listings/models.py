from django.db import models
from users.models import CustomUser 

# Create your models here.
class PropertyListing(models.Model):
    realtor = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)