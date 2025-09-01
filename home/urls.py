from django.urls import path, include

urlpatterns = [
    path('contact/', include('contact.urls')),
]