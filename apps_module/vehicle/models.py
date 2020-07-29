from django.db import models
from django.contrib.auth.models import User
from apps_module.company.models import CompanyProfile
from apps_module.apps_settings.models import (
    VehiclePurpose, VehicleType, VehicleFuelType, VehicleStatus)

# Create your models here.

VEHICLE_TYPE = (
    ("Salon", "Solon"),
    ("Pick Up", "Pick Up"),
    ("Mini Bus", "Mini Bus"),
    ("Bus", "Bus"),
    ("SUV", "SUV"),
    ("Truck", "Truck"),
    ("Other", "Other"),

)


FUEL_TYPE = (
    ("Petrol", "Petrol"),
    ("Diesel", "Diesel"),
    ("Kerosine", "Kerosine"),
    ("Other", "Other"),
)

VEHICLE_PURPOSE = (
    ("Hiring", "Hiring"),
    ("Transport", "Transport"),
    ("Cargo", "Cargo"),
    ("Other", "Other"),
)

VEHICLE_STATUS = (
    ("Good", "Good"),
    ("Bad", "Bad"),
    ("Other", "Other"),
)




class Vehicle(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    vehicle_code = models.CharField(
        max_length=100, null=True, blank=True)
    vehicle_registration_no = models.CharField(
        max_length=20, unique=True, null=False, blank=False)
    vehicle_type = models.CharField(
        max_length=20, choices=VEHICLE_TYPE,  null=True, blank=True)
    vehicle_manufacturer = models.CharField(
        max_length=20, null=True, blank=True)
    vehicle_model = models.CharField(max_length=20, null=True, blank=True)
    vehicle_color = models.CharField(max_length=20, null=True, blank=True)
    vehicle_fuel_type = models.CharField(max_length=20,
        choices=FUEL_TYPE,  null=True, blank=True)
    vehicle_purpose = models.CharField(max_length=20,
        choices=VEHICLE_PURPOSE,  null=True, blank=True)

    # vehicle_image = models.CharField(max_length=20, blank=True, null=True)
    vehicle_status = models.CharField(max_length=20,
        choices=VEHICLE_STATUS,  null=True, blank=True)
    vehicle_passenger_limit = models.IntegerField(null=True, blank=True)
    vehicle_cargo_limit = models.IntegerField(help_text="weight in kg", null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.vehicle_registration_no)
