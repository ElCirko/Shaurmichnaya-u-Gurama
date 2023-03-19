from rest_framework import serializers

from .models import Dish, Ingredient


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = (
            'id',
            'name',
            'get_absolute_url',
            'description',
            'price',
            'get_image',
            'get_thumbnail',
        )