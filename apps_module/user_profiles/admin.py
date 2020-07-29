from django.contrib import admin
from .models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'phone_number',
        'date_added',
        'date_updated',
    ]

    class Meta:
        model = UserProfile


admin.site.register(UserProfile, UserProfileAdmin)