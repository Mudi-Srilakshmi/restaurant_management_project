from django.db import models

class MenuItem(models.Model):
    """
    MenuItem model:
    - Stores details of each menu item (name, description, price, image).
    - ImageField is used for uploading and storing images in MEDIA folder.
    """

    name = models.CharField(max_length=100) # Name of the menu item
    description = models.TextField() # Short description
    price = models.DecimalField(max_digits=6, decimal_places=2) # Price
    image = models.ImageField(upload_to='menu_images/') # Upload folder: MEDIA/menu_images/ 

    def __str__(self):
        return self.name




