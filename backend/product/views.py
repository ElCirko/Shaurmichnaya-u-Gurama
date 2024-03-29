from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Dish, Ingredient
from .serializers import DishSerializer, IngredientSerializer


class LatestDishesList(APIView):
    def get(self, request, format=None):
        dishes = Dish.objects.all()[0:4]
        serializer = DishSerializer(dishes, many=True)
        return Response(serializer.data)


class DishDetail(APIView):
    def get_object(self, id):
        try:
            return Dish.objects.get(id=id)
        except Dish.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        dish = self.get_object(id)
        serializer = DishSerializer(dish)
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        dish = self.get_object(id)
        dish.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DishDetailBySlug(APIView):
    def get_object(self, slug):
        try:
            return Dish.objects.get(slug=slug)
        except Dish.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        dish = self.get_object(slug)
        serializer = DishSerializer(dish)
        return Response(serializer.data)


class DishList(APIView):
    def get(self, request, format=None):
        dishes = Dish.objects.all()
        serializer = DishSerializer(dishes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DishIngredients(APIView):
    def get_object(self, id):
        try:
            return Dish.objects.get(id=id)
        except Dish.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        ingredients = self.get_object(id).ingredients
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)


class IngredientList(APIView):
    def get(self, request, format=None):
        dishes = Ingredient.objects.all()
        serializer = IngredientSerializer(dishes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
