from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Dish
from .serializers import DishSerializer


class LatestDishesList(APIView):
    def get(self, request, format=None):
        dishes = Dish.objects.all()[0:4]
        serializer = DishSerializer(dishes, many=True)
        return Response(serializer.data)