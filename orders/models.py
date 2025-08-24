from django.db import models

# Django model to store restaurant location details
class RestaurantLocation(models.Model):
    """
    RestaurantLocation model:
    - Stores address, city, state, and zip code of restaurants.
    - Useful for keeping track of different restaurant branches or outlets.
    """

    # Street address of the restaurant (max length: 255 characters)
    address = models.CharField(max_length=255)

    # City where the restaurant is located (max length: 100 characters)
    city = models.CharField(max_length=100)

    # State where the restaurant is located (max length: 100 characters)
    state = models.CharField(max_length=100)

    # Zip code / postal code of the restaurant's location (max length: 10 characters)
    zip_code = models.CharField(max_length=10)

    # String representation of the object (helps when viewing in Django Admin)
    def __str__(self):
        return f"{self.address}, {self.city}, {self.state} - {self.zip_code}"


