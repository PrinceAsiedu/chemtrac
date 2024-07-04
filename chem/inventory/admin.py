from django.contrib import admin
from .models import Chemical, Formula, FormulaChemical


class FormulaChemicalInline(admin.TabularInline):
    model = FormulaChemical
    extra = 1

@admin.register(Formula)
class FormulaAdmin(admin.ModelAdmin):
    inlines = [FormulaChemicalInline]

admin.site.register(Chemical)
admin.site.register(FormulaChemical)