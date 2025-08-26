from django.db import models

# Option 2: Store restaurant info (name) in the database
class RestaurantInfo(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# existing model for addresses
class RestaurantAddress(models.Model):
    name = models.CharField(max_length=100) # Name of the restaurant branch
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}, {self.city}" 