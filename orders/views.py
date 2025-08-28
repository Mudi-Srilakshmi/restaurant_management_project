from django.shortcuts import render
from .models import MenuItem

def homepage(request):
    query = request.GET.get('q') # 'q' will come from the search input 
    if query:
        menu_items = MenuItem.objects.filter(name__icontains=query) # case-insensitive search
    else:
        menu_items = MenuItem.objects.all() # show all if no search
    return render(request, 'homepage.html', {'menu_items': menu_items, 'query': query})
