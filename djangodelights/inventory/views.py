from django.shortcuts import render
from .models import RecipeRequirements, MenuItem, Ingredient, Purchase
from .forms import IRecipeRequirementsForm, MenuItemForm, IngredientForm, PurchaseForm
from django.views.generic import TemplateView, ListView
from django.db.models import Sum
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'inventory/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menue_items'] = MenuItem.objects.all()
        context['purchases'] = Purchase.objects.all()
        context['ingredients'] = Ingredient.objects.all()
        return context


class IngredientList(ListView):
    model = Ingredient
    template_name = 'inventory/ingredient_list.html'

class UpdateIngredientsView(UpdateView):
    template_name = 'inventory/ingredient_update.html'
    model = Ingredient
    form_class = IngredientForm

class RecipeRequirementsList(ListView):
    model = RecipeRequirements
    template_name = 'inventory/recipe_requirements_list.html'

class MenuItemList(ListView):
    model = MenuItem    
    template_name = 'inventory/menu_item_list.html'

class PurchaseList(ListView):
    model = Purchase   
    template_name = 'inventory/purchase_list.html' 

class FinancialsView(TemplateView):
    template_name = 'inventory/financials.html' 


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['purchases'] = Purchase.objects.all()

        revenue = 0
        for purchase in Purchase.objects.all():
            revenue += purchase.menu_item.price

        total_cost = 0
        for purchase in Purchase.objects.all():
            for recipe_requirement in purchase.menu_item.reciperequirements_set.all():
                total_cost += recipe_requirement.ingredient.price_per_unit * recipe_requirement.quantity

        context['revenue'] = revenue
        context['total_cost'] = total_cost
        context['profit'] = revenue - total_cost
        return context