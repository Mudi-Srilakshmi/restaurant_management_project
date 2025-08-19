from django.conf import settings
from django.shortcuts import render

def home(request):
    context = {
        "restaurant_name": "My Restaurant",
        "phone_number": settings.RESTAURANT_PHONE,
    }
    return render(request, "home/home.html", context)
    
        