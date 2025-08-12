from django.db import models

# Model to represent a Menu item in the restaurant
class Menu(models.Model):
    # Name of the dish
    name = models.CharField(max_length=100)
    # Detailed description of the dish
    description = models.TextField()
    # Price of the dish (max_digits=8, decimal_places=2)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    # String representation of the model (shown in admin and elsewhere)
    def __str__(self):
        return self.name

# Model to represent a customer's order
class Order(models.Model):
    # ForeignKey links each order to a specific menu item
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    # Quantity ordered
    quantity = models.PositiveIntegerField(default=1)
    # Timestamp when the order was created (auto-set on creation)
    order_time = models.DateTimeField(auto_now_add=True)

    # String representation showing quantity and menu item name
    def __str__(self):
        return f"{self.quantity} * {self.menu_item.name}"

