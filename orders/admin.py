from django.contrib import admin
from .models import Restaurant

# Register Restaurant model so we can add phone number from admin panel
admin.site.register(Restaurant)