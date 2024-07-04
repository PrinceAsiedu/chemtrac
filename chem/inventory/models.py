from django.db import models

# Create your models here.
class Chemical(models.Model):
    name = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Formula(models.Model):
    name = models.CharField(max_length=100)
    chemicals = models.ManyToManyField(Chemical, through='FormulaChemical')

    def __str__(self):
        return self.name

class FormulaChemical(models.Model):
    formula = models.ForeignKey(Formula, on_delete=models.CASCADE)
    chemical = models.ForeignKey(Chemical, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)  # For example, in grams

    def __str__(self):
        return f"{self.quantity} of {self.chemical.name} in {self.formula.name}"
