from django.shortcuts import render
from .models import Restaurant

def homepage(request):
    # Get the first restaurant from the database
    restaurant = Restaurant.objects.first() # Fetch th restaurant

    return render(request, "homepage.html", {"restaurant": restaurant})
    