from django.db import models
from django.contrib.auth.models import User
from listings.models import PropertyListing  # Assuming you have a PropertyListing model
from django.conf import settings

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
    property_listing = models.ForeignKey(PropertyListing, on_delete=models.CASCADE)  # Property being booked
    booking_date = models.DateTimeField(auto_now_add=True)  # Date when the booking was made
    start_date = models.DateField()  # Start date of the booking
    end_date = models.DateField()  # End date of the booking
    status = models.CharField(max_length=20, default='Pending')  # Status of the booking (e.g., Pending, Confirmed, Cancelled)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.property_listing.title} from {self.start_date} to {self.end_date}"