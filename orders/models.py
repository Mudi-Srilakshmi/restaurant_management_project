from django.db import models
from django.contrib.auth.models import User

# UserProfile model to extend the built-in Django User
class UserProfile(models.Model):
    # One-to-One relationship with the built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'profile')

    # Additional profile fields
    name = models.CharField(max_length=100) # Full name of the user
    email = models.EmailField(max_length=254) # Email address of the user
    phone_number = models.CharField(max_length=15, blank=True, null=True) # Optional phone number

    def __str__(self):
        # This will display in the admin and when printing the object
        return f"{self.user.username}'s Profile" 



