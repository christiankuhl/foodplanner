from django.db import models

# Create your models here.
class Ingredient(models.Model):
        account = models.CharField(max_length=255)
        member = models.CharField(max_length=255)
        ref_meal = models.CharField(max_length=255,blank=True)
        ref_date = models.DateField(blank=True)
        ingredient = models.CharField(max_length=255)
        created = models.DateTimeField(auto_now_add=True)
        ingredient_there = models.BooleanField()
