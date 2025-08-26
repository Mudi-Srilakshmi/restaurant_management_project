from django.shortcuts import render, redirect
from .models import RestaurantInfo, RestaurantAddress, Contact
from .forms import ContactForm # Import the form

def homepage(request):
    """
    Homepage view:
    - Fetch restaurant name
    - Fetch all addresses
    - Handle contact form submission
    """
    # Restaurant name
    restaurant = RestaurantInfo.objects.first()
    restaurant_name = restaurant.name if restaurant else "Restaurant"

    # Restaurant addresses
    addresses = RestaurantAddress.objects.all()

    # Handle contact form submission
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() # Save submission to database
            return redirect('homepage') # Redirect to homepage
    else:
        form = ContactForm()

    context = {
        'restaurant_name': restaurant_name,
        'addresses': addresses,
        'form': form
    }

    return render(request, 'home/homepage.html', context)
  

    