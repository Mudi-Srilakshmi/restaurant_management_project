from django.urls import path
from .views import contact_view
from django.shortcuts import render

urlpatterns = [
    path("contact/", contact_view, name="contact"),
    path("success/", lambda request: render(request, "orders/success.html"), name="contact_success"),
]
