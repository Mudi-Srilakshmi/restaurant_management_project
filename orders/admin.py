from django.contrib import admin
from .models import RestaurantInfo, RestaurantAddress

# Register both models to manage from admin
admin.site.register(RestaurantInfo)
admin.site.register(RestaurantAddress)