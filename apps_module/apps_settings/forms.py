from django import forms
from .models import Position, Department, Employee, CarType


# class VehicleTypeForm(forms.ModelForm):
# 	class Meta:
# 		model = VehicleType
# 		fields = ["vehicle_type"]

# 	# def __init__(self, *args, **kwargs):
# 	# 	super(GeotechSupervisionDataForm, self).__init__(*args, **kwargs)
# 	# 	self.fields['project'].queryset = Project.objects.filter(
# 	# 		program="Geotechnical", project_status="Started").order_by("project_code")

class PositionForm(forms.ModelForm):
	class Meta:
		model = Position
		fields = ["position_name"]


class DepartmentForm(forms.ModelForm):
	class Meta:
		model = Department
		fields = ["department_name"]


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
                    "position",
                    "department", ]
    date_of_birth = forms.DateField(
        widget=forms.DateInput(format='%d-%m-%Y'),
        input_formats=('%d-%m-%Y', )
    )


class CarTypeForm(forms.ModelForm):
	class Meta:
		model = CarType
		fields = ["car_type"]
