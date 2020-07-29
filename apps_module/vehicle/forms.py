from django import forms
from .models import Vehicle


class VehicleForm(forms.ModelForm):
	class Meta:
		model = Vehicle
		fields = ["vehicle_code",
                    "vehicle_registration_no",
                    "vehicle_type",
                    "vehicle_manufacturer",
                    "vehicle_model",
                    "vehicle_color",
                    "vehicle_fuel_type",
                    "vehicle_purpose",
                    "vehicle_status",
                    "vehicle_passenger_limit",
                    "vehicle_cargo_limit",]
