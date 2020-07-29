from django import forms
from django.contrib.auth.models import User
from .models import Income, Expenses
from apps_module.vehicle.models import Vehicle
from apps_module.company.models import CompanyProfile



# def get_user_company(request, *args, **kwargs):
#     user = re



class IncomeForm(forms.ModelForm):


    class Meta:
        model = Income
        fields = ["date_of_income",
                  "vehicle",
                  "amount",
                  "source_of_income",
                  "income_description", ]
    date_of_income = forms.DateField(
        widget=forms.DateInput(format='%d-%m-%Y'),
        input_formats=('%d-%m-%Y', )
    )

    def __init__(self, *args, **kwargs):
        user = self.user = kwargs.pop('user')
        super(IncomeForm, self).__init__(*args, **kwargs)
        company_prof_obj = CompanyProfile.objects.get(user=user)
        self.fields['vehicle'].queryset = Vehicle.objects.filter(company=company_prof_obj)


class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ["date_of_expense",
                  "vehicle",
                  "amount",
                  "type_of_expenditure",
                  "expenditure_description",
                  "receipt_number", ]
    date_of_expense = forms.DateField(
        widget=forms.DateInput(format='%d-%m-%Y'),
        input_formats=('%d-%m-%Y', )
    )

    def __init__(self, *args, **kwargs):
        user = self.user = kwargs.pop('user')
        super(ExpensesForm, self).__init__(*args, **kwargs)
        company_prof_obj = CompanyProfile.objects.get(user=user)
        self.fields['vehicle'].queryset = Vehicle.objects.filter(
            company=company_prof_obj)
