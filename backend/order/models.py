from django.contrib.auth.models import User
from django.db import models

from product.models import Dish


class OrderItem(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.dish.name} ({self.quantity})"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    order_items = models.ManyToManyField(OrderItem)

    def total(self):
        total = 0
        for item in self.order_items.all():
            total += item.dish.price * item.quantity
        return total
