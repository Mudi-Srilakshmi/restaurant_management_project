from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100) # Name of the menu item
    description = models.TextField(blank=True, null=True) # Optional description
    price = models.DecimalField(max_digits=6, decimal_places=2) # Price of the item
    is_available = models.BooleanField(default=True) # Availability status

    def __str__(self):
        return self.name
        
