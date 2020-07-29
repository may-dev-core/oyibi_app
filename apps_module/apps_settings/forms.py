from django import forms
from .models import VehicleType, VehicleFuelType, VehicleStatus, TypeOfExpense, Employee, Position, VehiclePurpose, SourceOfIncome


class VehicleTypeForm(forms.ModelForm):
	class Meta:
		model = VehicleType
		fields = ["vehicle_type"]

	# def __init__(self, *args, **kwargs):
	# 	super(GeotechSupervisionDataForm, self).__init__(*args, **kwargs)
	# 	self.fields['project'].queryset = Project.objects.filter(
	# 		program="Geotechnical", project_status="Started").order_by("project_code")


class VehiclePurposeForm(forms.ModelForm):
	class Meta:
		model = VehiclePurpose
		fields = ["purpose_name"]


class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ["employee_id",
                    "first_name",
                    "last_name",
                    "date_of_birth",
                    "gender",
                    "location",
                    "phone_number_1",
                    "phone_number_2",
                    "position"]
