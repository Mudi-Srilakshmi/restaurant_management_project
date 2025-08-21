from django.db import models

# Feedback model to store customer comments in the database
class Feedback(models.Model):
    # "Comment" field where customer can type their feedback
    comment = models.TextField()

    # Automatically store the date & time when feedback is created  
    created_at = models.DateTimeField(auto_now_add=True)

    # String representation of the model (useful in Django Admin)
    def __str__(self):
        # Show only first 30 characters of comment for readability
        return f"Feedback {self.id} - {self.comment[:30]}"