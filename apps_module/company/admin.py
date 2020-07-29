from django.contrib import admin

from .models import CompanyProfile

# Register your models here.


@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "company_name",
        "company_address",
        "company_location",
        "company_phone_number",
        "date_added",
        "date_updated",
    ]

    class Meta:
        model = CompanyProfile

