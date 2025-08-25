from django.db import models

class ContactSubmission(models.Model):
    """
    ContactSubmission model:
    - Stores basic contact form details.
    - Fields: name (user's name) and email (user's email address).
    - Useful for saving user inquiries or contact requests.
    """

    # Full name of the user submitting the contact form (max length: 100 characters)
    name = models.CharField(max_length=100)

    # Email address of the user submitting the contact form
    email = models.EmailField()

    # String representation of the object (helps when viewing in Django Admin)
    def __str__(self):
        return f"{self.name} - {self.email}"