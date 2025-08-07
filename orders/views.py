from django.shortcuts import render
from .models import MenuItem
from django.http import JsonResponse

def menu_api(request):
    items = MenuItem.objects.all()
    data = [
        {
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'price': float(item.price)
        }
        for item in items
    ]
    return JsonResponse(data, safe=False)
