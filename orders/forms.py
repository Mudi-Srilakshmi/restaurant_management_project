from django import forms

# ContactForm class using Django's Form class
class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        label="Your Name"
    )
    email = forms.EmailField( # EmailField does email validation automatically
        required=True,
        label="Your Email"
    )
    message = forms.CharField(
        widget=forms.Textarea, # textarea instead of single-line input
        required=True,
        label="Your Message"
    )
    