from django.shortcuts import render
from .models import MenuItem

def menu(request):
    """
    Menu view:
    - Fetch all menu items (including images)
    - send them to template
    """
    items = MenuItem.objects.all()
    return render(request, 'orders/menu.html', {'items': items})
    