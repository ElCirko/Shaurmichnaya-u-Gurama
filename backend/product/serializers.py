from rest_framework import serializers

from .models import Dish, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name')


class DishSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    
    class Meta:
        model = Dish
        fields = (
            'id',
            'name',
            'ingredients',
            'description',
            'price',
            'get_absolute_url',
            'get_image',
            'get_thumbnail',
        )
