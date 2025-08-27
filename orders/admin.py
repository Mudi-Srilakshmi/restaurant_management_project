from django.contrib import admin
from .models import RestaurantInfo, RestaurantAddress

# Register models in admin so we can add/edit restautant info and addresses
admin.site.register(RestaurantInfo)
admin.site.register(RestaurantAddress)

