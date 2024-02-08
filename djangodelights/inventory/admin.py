from django.contrib import admin
from .models import RecipeRequirements, MenuItem, Ingredient, Purchase

admin.site.register(RecipeRequirements)
admin.site.register(MenuItem)
admin.site.register(Ingredient)
admin.site.register(Purchase)