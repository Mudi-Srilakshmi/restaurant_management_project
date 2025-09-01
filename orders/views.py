from django.shortcuts import render, redirect
from .models import Product

def home_view(request):
    # Get cart from session, if not exist create empty
    cart = request.session.get('cart', {})

    # Count total quantity of items in cart
    total_items = sum(cart.values())

    return render(request, 'home.html', {'total_items': total_items})


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    # Add product to cart (increase quantity if already exists)
    cart[product_id] = cart.get(product_id, 0) + 1

    # Save cart back into seesion
    request.session['cart'] = cart
    return redirect('home')