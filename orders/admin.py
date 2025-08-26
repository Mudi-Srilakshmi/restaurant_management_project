from django.contrib import admin
from .models import Contact # Import the Contact model

# Register Contact model so admin can view submissions
admin.site.register(Contact)
