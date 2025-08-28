from django.urls import path, include

urlpatterns = [
    path('', include('orders.urls')), # homepage points to orders app
]