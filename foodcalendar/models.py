from django.db import models

# Create your models here.
class Day(models.Model):
        account = models.CharField(max_length=255)
        member = models.CharField(max_length=255)
        date = models.DateField()
        meal = models.CharField(max_length=255)
        whoiscooking = models.CharField(max_length=255,blank=True)
        ingredient = models.CharField(max_length=255,blank=True)
        created = models.DateTimeField(auto_now_add=True)
        ingredient_there = models.BooleanField()
