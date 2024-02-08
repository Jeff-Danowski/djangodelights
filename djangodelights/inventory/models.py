from django.db import models
from datetime import datetime

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length = 200)
    quantity = models.FloatField(default = 0.0)
    unit = models.CharField(max_length = 200)
    price_per_unit = models.FloatField(default = 0)

    def __str__(self):
        return f"{self.name} has {self.quantity} {self.unit} left and is {self.price_per_unit} per {self.unit}."

class MenuItem(models.Model):
    name = models.CharField(max_length = 200, unique = True)
    price = models.FloatField(default = 0.00)

    def __str__(self):
        return f"{self.name}"

class RecipeRequirements(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete = models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE)
    quantity = models.FloatField(default = 0.0)

    def __str__(self):
        return f"{self.quantity} {self.ingredient}(s) are needed in each {self.menu_item}"

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete = models.CASCADE)
    time_purchased = models.DateTimeField(default = datetime.now())

    def __str__(self):
        return f"{self.menu_item} was purchased {self.time_purchased}"

