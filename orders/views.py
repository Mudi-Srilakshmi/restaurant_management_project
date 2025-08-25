from django.shortcuts import render
from .models import MenuItem

def menu_view(request):
    """
    Fetches all MenuItem objects from database and passes them to the templates for rendering.
    """
    items = MenuItem.objects.all()
    return render(request, 'orders/menu.html', {'items': items})
    