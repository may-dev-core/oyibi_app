from django.db import models
from apps_module.company.models import CompanyProfile
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),

)


class Position(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    position = models.CharField(max_length=20, unique=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.position


class Employee(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    location = models.CharField(max_length=255, null=True, blank=True)
    phone_number_1 = models.CharField(max_length=255, null=True, blank=True)
    phone_number_2 = models.CharField(max_length=255, null=True, blank=True)
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.first_name)

    def get_employee_fullname(self):
        return str(self.first_name + " " + self.last_name)


class VehiclePurpose(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    purpose_name = models.CharField(max_length=20)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.purpose_name


class VehicleType(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=20)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vehicle_type


class VehicleFuelType(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    fuel_type = models.CharField(max_length=20)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fuel_type


class VehicleStatus(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    vehicle_status = models.CharField(max_length=20)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vehicle_status


class TypeOfExpense(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    type_of_expense = models.CharField(max_length=20)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type_of_expense


class SourceOfIncome(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    source_of_income = models.CharField(max_length=20)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.source_of_income
