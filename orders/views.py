from django.shortcuts import render
from .models import RestaurantInfo, RestaurantAddress

def homepage(request):
    """
    Homepage view:
    - Fetch restaurant info
    - Fetch restaurant addresses
    - send them to template
    """
    restaurant = RestaurantInfo.objects.first() # Get the first restaurant
    addresses = RestaurantAddress.objects.all() # Get all addresses

    context = {
        'restaurant': restaurant,
        'addresses': addresses,
        'opening_hours': restaurant.opening_hours if restaurant else {}
    }

    return render(request, 'orders/homepage.html', context)
    