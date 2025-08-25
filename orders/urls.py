from django.urls import path
from . import views

# URL patterns for this app
urlpatterns = [
   path('contact/', views.contact_view, name='contact'),
]