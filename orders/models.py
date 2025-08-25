from django.db import models

# This model stores the restaurant's address
class RestaurantAddress(models.Model):
    name = models.CharField(max_length=100) # Name of the restaurant
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}, {self.city}"