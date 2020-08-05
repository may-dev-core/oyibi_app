from apps_module.apps_settings.views import department
from django.db.models import Sum
from apps_module.apps_settings.models import Department, Employee
from apps_module.webview.views import company_profile
import urllib
from urllib.parse import urlencode
from urllib.request import urlopen
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core import serializers
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from rest_framework.response import Response

# from base.models import User
from django.views.decorators.csrf import csrf_exempt

import json
from datetime import datetime

from apps_module.company.models import CompanyProfile
from apps_module.washing_bay.models import WashingBaySales
# Create your views here.


def get_washing_bay_sales_summary_report(user):

    company_profile = CompanyProfile.objects.get(user=user)
    w_bay_obj = WashingBaySales.objects.filter(company=company_profile)

    bay_array = []
    bay_list = []

    # date = bay_sales_form.cleaned_data['date']
    #             car_type = bay_sales_form.cleaned_data['car_type']
    #             registration_number = bay_sales_form.cleaned_data['registration_number']
    #             body = bay_sales_form.cleaned_data['body']
    #             engine = bay_sales_form.cleaned_data['engine']
    #             under = bay_sales_form.cleaned_data['under']
    #             inside = bay_sales_form.cleaned_data['inside']
    #             blowing = bay_sales_form.cleaned_data['blowing']
    #             hoover = bay_sales_form.cleaned_data['hoover']
    #             amount = bay_sales_form.cleaned_data['amount']
    #             attendant = bay_sales_form.cleaned_data['attendant']

    for i in w_bay_obj:
        bay_list.append("")
        bay_list.append(str(i.registration_number))
        bay_list.append(str(i.car_type))
        # bay_list.append(str(i.body))
        # bay_list.append(str(i.engine))
        # bay_list.append(str(i.under))
        # bay_list.append(str(i.inside))
        # bay_list.append(str(i.blowing))
        # bay_list.append(str(i.hoover))
        bay_list.append(str(i.amount))
        bay_list.append(str(i.attendant.get_full_name()))

    bay_array = [bay_list[x: x + 5]
                 for x in range(0, len(bay_list), 5)]

    print(bay_array)

    return bay_array


def get_washing_bay_sales_report(user):

    company_profile_obj = CompanyProfile.objects.get(user=user)
    w_bay_obj = WashingBaySales.objects.filter(company=company_profile_obj)

    attendants_list = set(WashingBaySales.objects.filter(
        company=company_profile_obj).values_list('attendant', flat=True).order_by("-id"))


    bay_array = []
    bay_list = []

    for i in attendants_list:
        attendant = Employee.objects.get(id=i)
        sum_amount = w_bay_obj.filter(
            attendant=i).aggregate(
            Sum('amount'))['amount__sum']

        bay_list.append("")
        bay_list.append(str(attendant))
        bay_list.append(f'{sum_amount:,}')

    bay_array = [bay_list[x: x + 3]
                 for x in range(0, len(bay_list), 3)]

    print(bay_array)

    return bay_array


def washing_bay_report(request):

    # - using the user, select app settings by user company
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect("/")
    # elif(request.user.is_staff):
    #     return HttpResponseRedirect("/backend_dashboard")
    # else:
    #     pass

    user = request.user

    # company_profile_obj = CompanyProfile.objects.get(user=user)
    washing_bay_employees_obj = Employee.objects.filter(department=Department.objects.get(department_name="Washing Bay"))
    print(washing_bay_employees_obj)
    # company_vehicle_obj = Vehicle.objects.filter(company=company_profile_obj)
    # type_of_expenditure_obj = TypeOfExpense.objects.filter(
    #     company=company_profile_obj)

    # print(type_of_expenditure_obj)
    # print(company_vehicle_obj)

    # if request.method == "POST":
    #     print(json.loads(request.body.decode()))
    #     post_data = json.loads(request.body.decode())
    #     # print(post_data["phone_number"])

    #     date_from = post_data["date_from"]
    #     date_to = post_data["date_to"]
    #     vehicle = post_data["vehicle"]

    #     date_from = datetime.strptime(
    #         date_from, "%d-%m-%Y").date()

    #     date_to = datetime.strptime(
    #         date_to, "%d-%m-%Y").date()

    #     try:

    #         print(get_profit_loss_array_by_date(
    #             user, vehicle, date_from, date_to))

    #         if get_profit_loss_array_by_date(user, vehicle, date_from, date_to):
    #             result = {
    #                 "status_code": 200,
    #                 "message": "",
    #                 "data": get_profit_loss_array_by_date(user, vehicle, date_from, date_to),
    #             }

    #             return JsonResponse(result)
    #         else:
    #             result = {
    #                 "status_code": 400,
    #                 "message": ""
    #             }

    #             return JsonResponse(result)

    #     except Exception as e:
    #         print("----", e)
    #         result = {
    #             "status_code": 400,
    #             "message": "Error: Unable to read data."
    #         }
    #         return JsonResponse(result)

    context = {
        # "company_name": company_profile_obj.company_name,
        "employee_obj": washing_bay_employees_obj,
        # "type_of_expenditure_obj": type_of_expenditure_obj,
        "bay_array": get_washing_bay_sales_report(user)
    }
    return render(request, "washing_bay_report.html", context)
