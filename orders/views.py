from django.shortcuts import render
from .models import RestaurantAddress

def homepage(request):
    # Get all restaurant addresses from database
    addresses = RestaurantAddress.objects.all()

    # Pass the addresses to the template
    context = {
        'addresses': addresses
    }
    return render(request, 'orders/homepage.html', context)

    