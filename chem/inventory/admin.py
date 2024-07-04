from django.contrib import admin
from .models import Chemical, Formula, FormulaChemical


class FormulaChemicalInline(admin.TabularInline):
    model = FormulaChemical
    extra = 1
