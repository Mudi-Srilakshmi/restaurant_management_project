from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    logo = models.ImageField(upload_to='restaurant_logos/', blank=True, null=True)
    
    # New fields for information page
    history =models.TextField(blank=True, null=True)
    mission = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

