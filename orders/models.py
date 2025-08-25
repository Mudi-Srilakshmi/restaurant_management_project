from django.db import models

class MenuItem(models.Model):
    """
    MenuItem model:
    - name: name of the food item
    - description: short details about the item
    - price: price of the item
    - image: uploaded image (stored in MEDIA folder)
    """

    name = models.CharField(max_length=100) # Item name
    description = models.TextField() # Item description
    price = models.DecimalField(max_digits=6, decimal_places=2) # Price
    image = models.ImageField(upload_to='menu_images/') # Image upload path: MEDIA/menu_images/

    def __str__(self):
        return self.name
        