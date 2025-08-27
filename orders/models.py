from django.db import models

# Restaurant Information (name, description, etc.)
class RestaurantInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Restaurant Address
class RestaurantAddress(models.Model):
    restaurant = models.ForeignKey(RestaurantInfo, on_delete=models.CASCADE, related_name='addresses')
    address = models.TextField()

    def __str__(self):
        return f"{self.restaurant.name} - {self.address}"

