from django.db import models

class Contact(models.Model):
    """
    Model to store contact form submissions.
    Fields:
        - name: User's name
        - email: User's email address
        - submitted_at: Timestamp when the form is submitted
    """
    name = models.CharField(max_length=100) # User's name
    email = models.EmailField()
    submitted_at = models.DateTimeField(auto_now_add=True) # Submission time 

    def __str__(self):
        return f"{self.name} - {self.email}"
