from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('ingredients/', views.IngredientList.as_view(), name='ingredients'),
    path('ingredients/<pk>/update', views.UpdateIngredientsView.as_view(), name='ingredient_update'),
    path('menuitems/', views.MenuItemList.as_view(), name='menuitems'),
    path('financials/', views.FinancialsView.as_view(), name='financials'),
    path('purchases/', views.PurchaseList.as_view(), name='purchases'),

]