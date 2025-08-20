from django.shortcuts import render

# View to display a list of menu items
def menu_list(request):
    # Hardcoded list of menu items with name and price
    menu_items = [
        {"name": "Chicken Biryani", "price": 250},
        {"name": "Paneer Butter Masala", "price": 180},
        {"name": "Gulab Jamun", "price": 50},
        {"name": "Mirchi Bajji", "price": 30},
    ]

    # Context dictionary to pass data to the template
    context = {"menu_items": menu_items}

    # Render 'menu.html' template with the context
    return render(request, "menu.html", context)
   