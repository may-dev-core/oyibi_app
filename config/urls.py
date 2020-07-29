"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

# from apps_module.user_account.views import homepage, login, logout, dashboard, forgot_password
from apps_module.webview.views import (
    homepage, login, logout, dashboard, register, company_profile)

from apps_module.account.views import (income, edit_income, delete_income,
                                       expenses, edit_expenses, delete_expenses,
                                       profit_loss)
from apps_module.apps_settings.views import (vehicle_settings, add_vehicle_type,
                                             edit_vehicle_type, delete_vehicle_type,
                                             add_vehicle_purpose, edit_vehicle_purpose,
                                             delete_vehicle_purpose,
                                             employee, edit_employee)
from apps_module.vehicle.views import vehicle, edit_vehicle, delete_vehicle

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", homepage, name="homepage"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("register/", register, name="register"),
    path("company_profile/", company_profile, name="company_profile"),


    path("dashboard/", dashboard, name="dashboard"),


    # accounts
    path("income/", income, name="income"),
    path("edit_income/(?P<iid>\d+)/$", edit_income, name="edit_income"),
    path("delete_income/(?P<iid>\d+)/$", delete_income, name="delete_income"),


    path("expenses/", expenses, name="expenses"),
    path("edit_expenses/(?P<iid>\d+)/$", edit_expenses, name="edit_expenses"),
    path("delete_expenses/(?P<iid>\d+)/$", delete_expenses, name="delete_expenses"),



    path("profit_loss/", profit_loss, name="profit_loss"),

    # app settings
    path("vehicle_settings/", vehicle_settings,
         name="vehicle_settings"),

    path("add_vehicle_type/", add_vehicle_type,
         name="add_vehicle_type"),
    path("edit_vehicle_type/(?P<pid>\d+)/$",
         edit_vehicle_type, name="edit_vehicle_type"),
    path("delete_vehicle_type/", delete_vehicle_type, name="delete_vehicle_type"),




    path("add_vehicle_purpose/", add_vehicle_purpose,
         name="add_vehicle_purpose"),
    path("edit_vehicle_purpose/(?P<id>\d+)/$",
         edit_vehicle_purpose, name="edit_vehicle_purpose"),
    path("delete_vehicle_purpose/", delete_vehicle_purpose,
         name="delete_vehicle_purpose"),

    path("employee/", employee,
         name="employee"),
    path("edit_employee/(?P<id>\d+)/$",
         edit_employee, name="edit_employee"),

    path("vehicle/", vehicle,
         name="vehicle"),
    path("edit_vehicle/(?P<vid>\d+)/$",
         edit_vehicle, name="edit_vehicle"),
    path("delete_vehicle/", delete_vehicle,
         name="delete_vehicle"),


#     path("forgot_password/", forgot_password, name="forgot_password"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
