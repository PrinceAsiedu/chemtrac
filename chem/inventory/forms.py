# formulas/forms.py
from django import forms
from .models import Formula, FormulaChemical

class FormulaForm(forms.ModelForm):
    class Meta:
        model = Formula
        fields = ['name']

class FormulaChemicalForm(forms.ModelForm):
    class Meta:
        model = FormulaChemical
        fields = ['chemical', 'quantity']
