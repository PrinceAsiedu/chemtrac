# formulas/urls.py
from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.formula_list, name='formula_list'),
    path('inventory/<int:pk>/', views.formula_detail, name='formula_detail'),
    path('inventory/add/', views.add_formula, name='add_formula'),
    path('inventory/<int:formula_pk>/remove/<int:chemical_pk>/', views.remove_chemical, name='remove_chemical'),
]
