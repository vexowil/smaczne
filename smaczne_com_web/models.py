from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=80)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    opening_hours = models.CharField(max_length=50)
    delivery_time = models.DecimalField(max_digits=3, decimal_places=0)

class Menu(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

class User(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=9, blank=False)
