from django.contrib import admin
from .models import Vehicle

# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'vehicle_code',
        'vehicle_registration_no',
        'vehicle_type',
        'vehicle_manufacturer',
        'vehicle_model',
        'vehicle_color',
        'vehicle_fuel_type',
        'vehicle_purpose',
        'vehicle_status',
        'vehicle_passenger_limit',
        'vehicle_cargo_limit',
        'date_added',
        'date_updated',
    ]

    class Meta:
        model = Vehicle


admin.site.register(Vehicle, VehicleAdmin)
