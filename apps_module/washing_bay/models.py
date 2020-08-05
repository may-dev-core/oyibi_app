from django.db import models
from apps_module.company.models import CompanyProfile
from apps_module.apps_settings.models import Employee

from apps_module.apps_settings.models import CarType

from datetime import date, timedelta


# Create your models here.
class WashingBayPrices(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    car_type = models.ForeignKey(CarType, on_delete=models.CASCADE)
    body = models.FloatField(null=True, blank=True)
    engine = models.FloatField(null=True, blank=True)
    under = models.FloatField(null=True, blank=True)
    inside = models.FloatField(null=True, blank=True)
    blowing = models.FloatField(null=True, blank=True)
    hoover = models.FloatField(null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.car_type


class WashingBaySales(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    car_type = models.ForeignKey(CarType, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=20)
    body = models.BooleanField(default=False)
    engine = models.BooleanField(default=False)
    under = models.BooleanField(default=False)
    inside = models.BooleanField(default=False)
    blowing = models.BooleanField(default=False)
    hoover = models.BooleanField(default=False)
    amount = models.FloatField(default=0.00)
    attendant = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.registration_number
