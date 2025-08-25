from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    """
    View to handle contact form submission:
    - If request is POST, validate and save data.
    - If GET, display an empty form.
    """

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() # Save form data to ContactSubmission model
            return redirect('contact') # Redirect to same page after submission
    else:
        form = ContactForm()

    return render(request, 'orders/contact.html', {'form': form})
    


        

