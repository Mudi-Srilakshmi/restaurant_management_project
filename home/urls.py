from django.urls import path, include

urlpatterns = [
    path('', include('orders.urls')), # include orders app urls
]