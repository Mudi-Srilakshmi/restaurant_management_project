from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    """
    Forms for the user to submit name and email
    """
    class Meta:
        model = Contact
        fields = ['name', 'email'] # Only name and email fields
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
        }