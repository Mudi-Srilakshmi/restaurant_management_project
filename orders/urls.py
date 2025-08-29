from django.urls import path
from .import views

urlpatterns = [

    # Other URLS...

    # New URL for restaurant info page
    path('restaurant-info/', views.restaurant_info, name='restaurant_info'),
]
    