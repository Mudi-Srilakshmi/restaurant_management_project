from django import forms
from .models import Feedback

# FeedbackForm is connected to Feedback model (ModelForm)
# This makes it easier to create form fields automatically from the model 
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback # Connects to Feedback model
        fields = ['comment'] # Only use the "comment" field in form
        widgets = {
            # Textarea widget for better typing experience
            'comment': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Enter your feedback here...'
            }),
        }