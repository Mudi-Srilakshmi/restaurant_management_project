from django.urls import path
from .views import home_view, add_to_cart

urlpatterns = [
    path('', home_view, name='home'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
]