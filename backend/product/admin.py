from django.contrib import admin

from .models import Dish, Ingredient


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_added')
    prepopulated_fields = {"slug": ("name",)}
