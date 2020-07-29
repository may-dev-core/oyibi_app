from django.db import models
from apps_module.vehicle.models import Vehicle
from apps_module.company.models import CompanyProfile
from apps_module.apps_settings.models import TypeOfExpense, SourceOfIncome

# Create your models here.

SOURCE_OF_INCOME = {
    ("Hiring", "Hiring"),
    ("Delivery", "Delivery"),
    ("Transportation", "Transportation"),
    ("Other", "Other"),
}

TYPE_OF_EXPENSES = {
    ("Fuel", "Fuel"),
    ("Repairs", "Repairs"),
    ("General Servicing", "General Servicing"),
    ("Other", "Other"),
}


class Income(models.Model):
    date_of_income = models.DateField()
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    amount = models.FloatField()
    source_of_income = models.CharField(max_length=20, choices=SOURCE_OF_INCOME, null=True, blank=True)
    income_description = models.CharField(max_length=255, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.vehicle)


class Expenses(models.Model):
    date_of_expense = models.DateField()
    company = models.ForeignKey(
        CompanyProfile, on_delete=models.CASCADE, null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    type_of_expenditure = models.CharField(
        max_length=20,  choices=TYPE_OF_EXPENSES, blank=True, null=True)
    amount = models.FloatField()
    expenditure_description = models.CharField(max_length=255, blank=True, null=True)
    receipt_number = models.CharField(max_length=20, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.type_of_expenditure)
