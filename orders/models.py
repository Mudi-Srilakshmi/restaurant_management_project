from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField() # Menu item description
    price = models.DecimalField(max_digits=6, decimal_places=2) # Price
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    # New field for image, stored in MEDIA_ROOT/menu_images/

    def __str__(self):
        return self.name
        