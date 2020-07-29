from django.contrib import admin
from .models import (Position, Employee, VehicleStatus,
                     VehiclePurpose, VehicleFuelType, VehicleType, TypeOfExpense, SourceOfIncome)

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
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'position',
        'date_updated',
    ]

    class Meta:
        model = Position


@admin.register(VehiclePurpose)
class VehiclePurposeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'purpose_name',
        'date_updated',
    ]

    class Meta:
        model = VehiclePurpose


@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'vehicle_type',
        'date_updated',
    ]

    class Meta:
        model = VehicleType


@admin.register(VehicleFuelType)
class VehicleFuelTypeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'fuel_type',
        'date_updated',
    ]

    class Meta:
        model = VehicleFuelType


@admin.register(VehicleStatus)
class VehicleStatusAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'vehicle_status',
        'date_updated',
    ]

    class Meta:
        model = VehicleStatus


@admin.register(TypeOfExpense)
class TypeOfExpenseAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'type_of_expense',
        'date_updated',
    ]

    class Meta:
        model = TypeOfExpense


@admin.register(SourceOfIncome)
class SourceOfIncomeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'source_of_income',
        'date_updated',
    ]

    class Meta:
        model = SourceOfIncome
