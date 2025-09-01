from django.shortcuts import render
from .forms import ContactForm # Import the form

# Function-based view to handle the contact form
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST) # Bind data from request
        if form.is_valid(): # Django automatically checks email + required fields
            # Extract cleaned (validated) data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # For now, just print in terminal (Later you can save or send email)
            print("Contact Form Submitted:")
            print("Name:", name)
            print("Email:", email)
            print("Message:", message)

            return render(request, "contact/success.html", {"name": name})
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})
