from django.urls import path
from . import views

# URL patterns for this app
urlpatterns = [
    # URL 'menu/' will call the menu_list view
    path('menu/', views.menu_list, name='menu_list'),
]
