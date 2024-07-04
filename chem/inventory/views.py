# formulas/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Formula, Chemical, FormulaChemical
from .forms import FormulaForm, FormulaChemicalForm

def formula_list(request):
    formulas = Formula.objects.all()
    return render(request, 'formulas/formula_list.html', {'formulas': formulas})

def formula_detail(request, pk):
    formula = get_object_or_404(Formula, pk=pk)
    if request.method == 'POST':
        form = FormulaChemicalForm(request.POST)
        if form.is_valid():
            formula_chemical = form.save(commit=False)
            formula_chemical.formula = formula
            formula_chemical.save()
            return redirect('formula_detail', pk=formula.pk)
    else:
        form = FormulaChemicalForm()
    return render(request, 'formulas/formula_detail.html', {'formula': formula, 'form': form})

def add_formula(request):
    if request.method == 'POST':
        form = FormulaForm(request.POST)
        if form.is_valid():
            formula = form.save()
            return redirect('formula_detail', pk=formula.pk)
    else:
        form = FormulaForm()
    return render(request, 'formulas/formula_form.html', {'form': form})

def remove_chemical(request, formula_pk, chemical_pk):
    formula = get_object_or_404(Formula, pk=formula_pk)
    chemical = get_object_or_404(Chemical, pk=chemical_pk)
    formula.chemicals.remove(chemical)
    return redirect('formula_detail', pk=formula_pk)
