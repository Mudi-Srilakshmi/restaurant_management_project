from django.shortcuts import render
from .models import RestaurantInfo

def home(request):
    # get first restaurant entry
    restaurant = RestaurantInfo.objects.first()
    return render(request, "home.html", {"restaurant": restaurant})
