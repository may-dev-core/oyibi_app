from django.contrib import admin
from .models import (Position, Department, Employee, CarType)

# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'employee_id',
        'first_name',
        'last_name',
        'date_of_birth',
        'gender',
        'location',
        'phone_number_1',
        'phone_number_2',
        'position',
        'date_updated',
    ]

    class Meta:
        model = Employee


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'position_name',
        'date_updated',
    ]

    class Meta:
        model = Position


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'department_name',
        'date_updated',
    ]

    class Meta:
        model = Department


@admin.register(CarType)
class CarTypeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'car_type',
        'date_updated',
    ]

    class Meta:
        model = CarType
