from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            # Email subject and content
            subject = f"New Contact Form Submission from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            # Send email
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL, # Sender
                [settings.RESTAURANT_EMAIL], # receiver
            )

            # Redirect after success
            return redirect("contact_success")

    else:
        form = ContactForm()

    return render(request, "orders/contact.html", {"form": form})
    