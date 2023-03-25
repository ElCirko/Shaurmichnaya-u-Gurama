from rest_framework import serializers

from .models import Order, OrderItem
from product.models import Dish

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("dish", "quantity")


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "user",
            "created_at",
            "order_items",
            "total",
        )
        
    def update(self, instance, validated_data):
        instance.user = validated_data.get("user", instance.user)
        
        items = []
        for item in validated_data.get("order_items"):
            items.append(OrderItem.objects.get(dish__name=item.get("dish"), quantity=item.get("quantity")))
        instance.order_items.clear()
        instance.order_items.add(*items)
        instance.save()
        return instance