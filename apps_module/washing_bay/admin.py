from django.contrib import admin
from .models import WashingBaySales
# Register your models here.
@admin.register(WashingBaySales)
class WashingBaySalesAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        "date",
        "car_type",
        "body",
        "engine",
        "under",
        "inside",
        "blowing",
        "hoover",
        "amount",
        "attendant"
    ]

    class Meta:
        model = WashingBaySales
