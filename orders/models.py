from django.db import models

class RestaurantAddress(models.Model):
    """
    Model to store restaurant branch addresses
    """
    name = models.CharField(max_length=100) # Branch name
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True) # Optional for map
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True) # Optional for map

    def __str__(self):
        return f"{self.name}, {self.city}"

