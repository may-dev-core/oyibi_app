from apps_module.webview import models
from django import forms
from .models import WashingBayPrices, WashingBaySales

class WashingBayPricesForm(forms.ModelForm):
    class Meta:
        model = WashingBayPrices
        fields = ["car_type",
                    "body",
                    "engine",
                    "under",
                    "inside",
                    "blowing",
                    "hoover",]
    # date_of_birth = forms.DateField(
    #     widget=forms.DateInput(format='%d-%m-%Y'),
    #     input_formats=('%d-%m-%Y', )
    # )


class WashingBaySalesForm(forms.ModelForm):
    class Meta:
        model = WashingBaySales
        fields = [
            "date",
            "car_type",
            "registration_number",
            "body",
            "engine",
            "under",
            "inside",
            "blowing",
            "hoover",
            "amount",
            "attendant"
        ]
    date = forms.DateField(
        widget=forms.DateInput(format='%d-%m-%Y'),
        input_formats=('%d-%m-%Y', )
    )