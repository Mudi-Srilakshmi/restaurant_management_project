from django.db import models
from django.contrib.auth.models import User

# Assuming Menu model is defined elsewhere in your app
class Order(models.Model):
    # Link to the user who placed the order
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Customer"
    )

    # Many-to-many relationship with Menu items (order can have multiple dishes)
    order_items = models.ManyToManyField(
        'Menu',
        verbose_name="Order Items"
    )

    # Total price of the order
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Total Amount"
    )

    # Choices for the current status of the order

    STATUS_CHOICES =[
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    order_status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PENDING',
        verbose_name="Order Status"
    )

    # Automatically store the datetime when the order was created
    order_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Order Time"
    )

    def __str__(self):
        # Display useful info about the order
        return f"Order #{self.id} by {self.customer.username} - {self.order_status}"