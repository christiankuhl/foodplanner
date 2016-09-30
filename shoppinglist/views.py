from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from shoppinglist.models import Ingredient
from shoppinglist.serializers import IngredientSerializer

# Create your views here.
class ShoppingView(viewsets.ModelViewSet):
    # this fetches all the rows of data in the Fish table
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
