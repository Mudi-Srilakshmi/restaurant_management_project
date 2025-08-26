from django.shortcuts import render
from .models import MenuItem

def menu(request):
    # Fetch all available menu items
    items = MenuItem.objects.filter(is_available=True)

    # Pass them to the template
    context = {
        'items': items
    }
    return render(request, 'home/menu.html', context) # Template path
    