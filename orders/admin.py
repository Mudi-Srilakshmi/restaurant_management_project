from django.contrib import admin
from .models import RestaurantInfo, RestaurantAddress

admin.site.register(RestaurantInfo)
admin.site.register(RestaurantAddress)

