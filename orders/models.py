from django.db import models

class RestaurantInfo(models.Model):
    # Restaurant basic info
    name = models.CharField(max_length=200)
    description = models.TextField()

    # Opening hours stored as JSON (e.g., {"Mon": "9 AM - 9 PM", "Tue": "Closed"})
    opening_hours = models.JSONField(default=dict)

    def __str__(self):
        return self.name

class RestaurantAddress(models.Model):
    restaurant = models.ForeignKey(RestaurantInfo, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.address
        