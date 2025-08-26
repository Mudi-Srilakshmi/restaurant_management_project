from django.shortcuts import render
from .models import RestaurantInfo, RestaurantAddress

def homepage(request):
    """
    view for the homepage
    Fetches restaurant name and addresses
    """
    # Fetch restaurant name
    restaurant = RestaurantInfo.objects.first()
    restaurant_name = restaurant.name if restaurant else "Restaurant"

    # Fetch all restaurant addresses
    addresses = RestaurantAddress.objects.all()

    context = {
        'restaurant_name': restaurant_name,
        'addresses': addresses
    }
    return render(request, 'home/homepage.html', context) # Template path
    