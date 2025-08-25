from django.shortcuts import render
from .models import MenuItem

def menu_view(request):
    """
    View to display all menu items along with their uploaded images.
    - Fetches data from MenuItem model.
    - Sends it to the template for rendering.
    """
    items = MenuItem.objects.all() # Get all menu items
    return render(request, 'orders/menu.html', {'items': items})
    