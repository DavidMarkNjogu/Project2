from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from profiles.models import Profile

CustomUser  = get_user_model()

@receiver(post_save, sender=CustomUser )
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)  # Ensure this uses the CustomUser  instance

@receiver(post_save, sender=CustomUser )
def save_profile(sender, instance, **kwargs):
    instance.profile.save()  # This should work as expected