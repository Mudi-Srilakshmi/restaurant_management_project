from django.shortcuts import render
from .models import RestaurantInfo, RestaurantAddress

def homepage(request):
    # Fetch restaurant name (option 2)
    restaurant = RestaurantInfo.objects.first() # Get first entry
    restaurant_name = restaurant.name if restaurant else "Restaurant"

    # Fetch all restaurant addresses 
    addresses = RestaurantAddress.objects.all()

    context = {
        'restaurant_name': restaurant_name,
        'addresses': addresses
    }
    return render(request, 'home/homepage.html', context)
  