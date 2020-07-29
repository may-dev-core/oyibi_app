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
from django.db.models import Sum

# from base.models import User
from django.views.decorators.csrf import csrf_exempt

import json
from datetime import datetime, date

from apps_module.company.models import CompanyProfile
from apps_module.apps_settings.models import SourceOfIncome, TypeOfExpense
from apps_module.vehicle.models import Vehicle
from .models import Income, Expenses
from .forms import IncomeForm, ExpensesForm


def get_income_array():

    income_array = []
    income_list = []

    income_data_obj = Income.objects.all()
    for i in income_data_obj:
        income_list.append("")
        income_list.append(i.id)
        income_list.append(str(i.date_of_income))
        income_list.append(i.company.company_name)
        income_list.append(i.vehicle.vehicle_registration_no)
        income_list.append(str(i.amount))
        income_list.append(i.source_of_income.source_of_income)
        income_list.append(i.income_description)

    income_array = [income_list[x: x + 8]
                    for x in range(0, len(income_list), 8)]
    print(income_array)

    return income_array


def get_expenses_array():
    try:
        expenses_array = []
        expenses_list = []

        expenses_data_obj = Expenses.objects.all()
        for i in expenses_data_obj:
            expenses_list.append("")
            expenses_list.append(i.id)
            expenses_list.append(str(i.date_of_expense))
            expenses_list.append(i.company.company_name)
            expenses_list.append(i.vehicle.vehicle_registration_no)
            expenses_list.append(str(i.amount))
            expenses_list.append(i.type_of_expenses.type_of_expense)
            expenses_list.append(i.expense_description)
            expenses_list.append(i.receipt_number)

        expenses_array = [expenses_list[x: x + 9]
                          for x in range(0, len(expenses_list), 9)]
        print(expenses_array)

        return expenses_array
    except Exception as e:
        pass


def get_profit_loss_array(user, *args, **kwargs):
    try:
        pl_array = []
        pl_list = []

        company_profile_obj = CompanyProfile.objects.get(user=user)

        # vehicle_obj = Vehicle.objects.all()
        vehicle_obj = Vehicle.objects.filter(
            company=company_profile_obj).values_list('id', flat=True).order_by("-id")

        for i in vehicle_obj:

            single_vehicle_obj = Vehicle.objects.get(id=i)

            sum_income = Income.objects.filter(
                vehicle_id=i).aggregate(
                Sum('amount'))['amount__sum']

            sum_expense = Expenses.objects.filter(
                vehicle_id=i).aggregate(
                Sum('amount'))['amount__sum']

            profit_loss_vehicle = sum_income - sum_expense

            pl_list.append("")
            pl_list.append(company_profile_obj.company_name)
            pl_list.append(single_vehicle_obj.vehicle_registration_no)
            pl_list.append(f'{sum_income:,}')
            pl_list.append(f'{sum_expense:,}')
            pl_list.append(f'{profit_loss_vehicle:,}')

        pl_array = [pl_list[x: x + 6]
                    for x in range(0, len(pl_list), 6)]
        print(pl_array)

        return pl_array
    except Exception as e:
        print(e)
        pass


def get_profit_loss_array_by_date(user, vehicle, date_from, date_to):
    try:
        pl_array = []
        pl_list = []

        company_profile_obj = CompanyProfile.objects.get(user=user)

        if vehicle == "all":
            # vehicle_obj = Vehicle.objects.all()
            vehicle_obj = Vehicle.objects.filter(
                company=company_profile_obj).values_list('id', flat=True).order_by("-id")
        else:
            vehicle_obj = Vehicle.objects.filter(
                company=company_profile_obj, id=vehicle).values_list('id', flat=True).order_by("-id")

        print("ddd", vehicle_obj)

        for i in vehicle_obj:

            single_vehicle_obj = Vehicle.objects.filter(id=i)

            print(single_vehicle_obj)

            for x in single_vehicle_obj:
                try:
                    sum_income = Income.objects.filter(
                        vehicle=x.id, date_of_income__range=[date_from, date_to]).aggregate(
                        Sum('amount'))['amount__sum']
                    if sum_income is None:
                        sum_income = 0
                except Exception as e:
                    sum_income = 0

                print("--in--", sum_income)

                try:
                    sum_expense = Expenses.objects.filter(
                        vehicle_id=x.id, date_of_expense__range=[date_from, date_to]).aggregate(
                        Sum('amount'))['amount__sum']
                    if sum_expense is None:
                        sum_expense = 0
                except Exception as e:
                    sum_expense = 0

                print("--xp--", sum_income)

                try:
                    profit_loss_vehicle = sum_income - sum_expense

                except Exception as identifier:
                    print("error")
                    profit_loss_vehicle = 0

                pl_list.append("")
                pl_list.append(company_profile_obj.company_name)
                pl_list.append(x.vehicle_registration_no)
                pl_list.append(f'{sum_income:,}')
                pl_list.append(f'{sum_expense:,}')
                pl_list.append(f'{profit_loss_vehicle:,}')

        pl_array = [pl_list[x: x + 6]
                    for x in range(0, len(pl_list), 6)]
        print(pl_array)

        return pl_array
    except Exception as e:
        print("-----", e)
        pass


# def income(request):

#     # - using the user, select app settings by user company
#     # if not request.user.is_authenticated:
#     #     return HttpResponseRedirect("/")
#     # elif(request.user.is_staff):
#     #     return HttpResponseRedirect("/backend_dashboard")
#     # else:
#     #     pass

#     user = request.user

#     company_profile_obj = CompanyProfile.objects.get(user=user)
#     company_vehicle_obj = Vehicle.objects.filter(company=company_profile_obj)
#     source_of_income_obj = SourceOfIncome.objects.filter(
#         company=company_profile_obj)

#     income_obj = Income.objects.all()

#     print(source_of_income_obj)
#     print(company_vehicle_obj)

#     if request.method == "POST":
#         print(json.loads(request.body.decode()))
#         post_data = json.loads(request.body.decode())
#         # print(post_data["phone_number"])

#         income_date = post_data["income_date"]
#         vehicle = post_data["vehicle"]
#         amount = post_data["amount"]
#         source_of_income = post_data["source_of_income"]
#         income_description = post_data["income_description"]

#         income_date = datetime.strptime(
#             income_date, "%m-%d-%Y").date()

#         try:

#             income_obj = Income.objects.create(
#                 date_of_income=income_date,
#                 company=company_profile_obj,
#                 vehicle=Vehicle.objects.get(id=vehicle),
#                 amount=amount,
#                 source_of_income=SourceOfIncome.objects.get(
#                     id=source_of_income),
#                 income_description=income_description
#             )

#             if income_obj:
#                 result = {
#                     "status_code": 200,
#                     "message": "Income successfully added.",
#                     "data": get_income_array(),
#                 }

#                 return JsonResponse(result)
#             else:
#                 result = {
#                     "status_code": 400,
#                     "message": "Error: Unable to add income"
#                 }

#                 return JsonResponse(result)

#         except Exception as e:
#             result = {
#                 "status_code": 400,
#                 "message": "Error: Unable to add income"
#             }

#     context = {
#         "company_name": company_profile_obj.company_name,
#         "company_vehicle_obj": company_vehicle_obj,
#         "source_of_income_obj": source_of_income_obj,
#         "income_array": get_income_array(),
#         "income_obj": income_obj
#     }
#     return render(request, "income.html", context)


def income(request):

    user = request.user

    company_profile_obj = CompanyProfile.objects.get(user=user)

    income_obj = Income.objects.filter(company=company_profile_obj)

    income_form = IncomeForm(request.POST or None, user=user)

    if request.method == "POST":
        print(request.POST)
        if income_form.is_valid():
            # post_data = json.loads(request.body.decode())
            # print(post_data["phone_number"])

            date_of_income = income_form.cleaned_data["date_of_income"]
            vehicle = income_form.cleaned_data["vehicle"]
            amount = income_form.cleaned_data["amount"]
            source_of_income = income_form.cleaned_data["source_of_income"]
            income_description = income_form.cleaned_data["income_description"]

            # date_of_income = datetime.strptime(
            #     date_of_income, "%m-%d-%Y").date()

            try:

                Income(
                    date_of_income=date_of_income,
                    company=company_profile_obj,
                    vehicle=vehicle,
                    amount=amount,
                    source_of_income=source_of_income,
                    income_description=income_description
                ).save()

                
                print("success")


            except Exception as e:
                raise e
                print(e)
            return HttpResponseRedirect('/income')

    context = {
        "company_name": company_profile_obj.company_name,
        # "company_vehicle_obj": company_vehicle_obj,
        # "source_of_income_obj": source_of_income_obj,
        # "income_array": get_income_array(),
        "income_obj": income_obj,
        "income_form": income_form,
    }
    return render(request, "income.html", context)


def edit_income(request, iid):

    user = request.user

    company_profile_obj = CompanyProfile.objects.get(user=user)
    income_obj = Income.objects.filter(company=company_profile_obj)
    instance = get_object_or_404(Income, id=iid)
    edit_income_form = IncomeForm(request.POST or None, instance=instance, user=user)


    if request.method == "POST":
        print(request.POST)
        if edit_income_form.is_valid():
            # post_data = json.loads(request.body.decode())
            # print(post_data["phone_number"])

            date_of_income = edit_income_form.cleaned_data["date_of_income"]
            vehicle = edit_income_form.cleaned_data["vehicle"]
            amount = edit_income_form.cleaned_data["amount"]
            source_of_income = edit_income_form.cleaned_data["source_of_income"]
            income_description = edit_income_form.cleaned_data["income_description"]

            # date_of_income = datetime.strptime(
            #     date_of_income, "%m-%d-%Y").date()

            try:

                Income.objects.filter(id=iid).update(
                    date_of_income=date_of_income,
                    company=company_profile_obj,
                    vehicle=vehicle,
                    amount=amount,
                    source_of_income=source_of_income,
                    income_description=income_description
                )

                print("--update--")

            except Exception as e:
                raise e
                print(e)
            return HttpResponseRedirect('/income')

    context = {
        "company_name": company_profile_obj.company_name,
        # "company_vehicle_obj": company_vehicle_obj,
        # "source_of_income_obj": source_of_income_obj,
        # "income_array": get_income_array(),
        "income_obj": income_obj,
        "edit_income_form": edit_income_form,
    }
    return render(request, "income_edit.html", context)


def delete_income(request, iid):

    Income.objects.get(id=iid).delete()
    print('deleted')
    return HttpResponseRedirect('/income')


# def expense(request):

#     # - using the user, select app settings by user company
#     # if not request.user.is_authenticated:
#     #     return HttpResponseRedirect("/")
#     # elif(request.user.is_staff):
#     #     return HttpResponseRedirect("/backend_dashboard")
#     # else:
#     #     pass

#     user = request.user

#     company_profile_obj = CompanyProfile.objects.get(user=user)
#     company_vehicle_obj = Vehicle.objects.filter(company=company_profile_obj)
#     type_of_expenditure_obj = TypeOfExpense.objects.filter(
#         company=company_profile_obj)

#     print(type_of_expenditure_obj)
#     print(company_vehicle_obj)

#     if request.method == "POST":
#         print(json.loads(request.body.decode()))
#         post_data = json.loads(request.body.decode())
#         # print(post_data["phone_number"])

#         expense_date = post_data["expense_date"]
#         vehicle = post_data["vehicle"]
#         amount = post_data["amount"]
#         type_of_expenditure = post_data["type_of_expenditure"]
#         expense_description = post_data["description"]
#         receipt_number = post_data["receipt_number"]

#         expense_date = datetime.strptime(
#             expense_date, "%m-%d-%Y").date()

#         try:

#             expenses_obj = Expenses.objects.create(
#                 date_of_expense=expense_date,
#                 company=company_profile_obj,
#                 vehicle=Vehicle.objects.get(id=vehicle),
#                 amount=amount,
#                 type_of_expenses=TypeOfExpense.objects.get(
#                     id=type_of_expenditure),
#                 expense_description=expense_description,
#                 receipt_number=receipt_number
#             )

#             if expenses_obj:
#                 result = {
#                     "status_code": 200,
#                     "message": "Expenditure successfully added.",
#                     "data": get_expenses_array(),
#                 }

#                 return JsonResponse(result)
#             else:
#                 result = {
#                     "status_code": 400,
#                     "message": "Error: Unable to add expenditure."
#                 }

#                 return JsonResponse(result)

#         except Exception as e:
#             result = {
#                 "status_code": 400,
#                 "message": "Error: Unable to add expenditure."
#             }

#     context = {
#         "company_name": company_profile_obj.company_name,
#         "company_vehicle_obj": company_vehicle_obj,
#         "type_of_expenditure_obj": type_of_expenditure_obj,
#         "expense_array": get_expenses_array()
#     }
#     return render(request, "expense.html", context)





def expenses(request):

    user = request.user

    company_profile_obj = CompanyProfile.objects.get(user=user)

    expense_obj = Expenses.objects.filter(company=company_profile_obj)

    expenses_form = ExpensesForm(request.POST or None, user=user)

    if request.method == "POST":
        print(request.POST)
        if expenses_form.is_valid():
            # post_data = json.loads(request.body.decode())
            # print(post_data["phone_number"])

            date_of_expense = expenses_form.cleaned_data["date_of_expense"]
            vehicle = expenses_form.cleaned_data["vehicle"]
            amount = expenses_form.cleaned_data["amount"]
            type_of_expenditure = expenses_form.cleaned_data["type_of_expenditure"]
            expenditure_description = expenses_form.cleaned_data["expenditure_description"]
            receipt_number = expenses_form.cleaned_data["receipt_number"]

            # date_of_expense = datetime.strptime(
            #     date_of_expense, "%Y-%m-%d").date()

            try:

                Expenses(
                    date_of_expense=date_of_expense,
                    company=company_profile_obj,
                    vehicle=vehicle,
                    amount=amount,
                    type_of_expenditure=type_of_expenditure,
                    expenditure_description=expenditure_description,
                    receipt_number=receipt_number,
                ).save()

                print("success")

            except Exception as e:
                raise e
                print(e)
            return HttpResponseRedirect('/expenses')

    context = {
        "company_name": company_profile_obj.company_name,
        # "company_vehicle_obj": company_vehicle_obj,
        # "source_of_expense_obj": source_of_expense_obj,
        # "income_array": get_income_array(),
        "expense_obj": expense_obj,
        "expenses_form": expenses_form,
    }
    return render(request, "expenses.html", context)


def edit_expenses(request, iid):

    user = request.user
    company_profile_obj = CompanyProfile.objects.get(user=user)
    expense_obj = Expenses.objects.filter(company=company_profile_obj)

    instance = get_object_or_404(Expenses, id=iid)
    expenses_form = ExpensesForm(request.POST or None, instance=instance, user=user)

    if request.method == "POST":
        print(request.POST)
        if expenses_form.is_valid():
            # post_data = json.loads(request.body.decode())
            # print(post_data["phone_number"])

            date_of_expense = expenses_form.cleaned_data["date_of_expense"]
            vehicle = expenses_form.cleaned_data["vehicle"]
            amount = expenses_form.cleaned_data["amount"]
            type_of_expenditure = expenses_form.cleaned_data["type_of_expenditure"]
            expenditure_description = expenses_form.cleaned_data["expenditure_description"]
            receipt_number = expenses_form.cleaned_data["receipt_number"]

            # date_of_income = datetime.strptime(
            #     date_of_income, "%m-%d-%Y").date()

            try:

                Expenses.objects.filter(id=iid).update(
                    date_of_expense=date_of_expense,
                    company=company_profile_obj,
                    vehicle=vehicle,
                    amount=amount,
                    type_of_expenditure=type_of_expenditure,
                    expenditure_description=expenditure_description,
                    receipt_number=receipt_number,
                )

                print("--updated--")

            except Exception as e:
                raise e
                print(e)
            return HttpResponseRedirect('/expenses')

    context = {
        # "company_name": company_profile_obj.company_name,
        "expense_obj": expense_obj,
        "expenses_form": expenses_form,
    }
    return render(request, "expenses_edit.html", context)


def delete_expenses(request, iid):

    Expenses.objects.get(id=iid).delete()
    print('deleted')
    return HttpResponseRedirect('/expenses')

def profit_loss(request):

    # - using the user, select app settings by user company
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect("/")
    # elif(request.user.is_staff):
    #     return HttpResponseRedirect("/backend_dashboard")
    # else:
    #     pass

    user = request.user

    company_profile_obj = CompanyProfile.objects.get(user=user)
    company_vehicle_obj = Vehicle.objects.filter(company=company_profile_obj)
    type_of_expenditure_obj = TypeOfExpense.objects.filter(
        company=company_profile_obj)

    print(type_of_expenditure_obj)
    print(company_vehicle_obj)

    if request.method == "POST":
        print(json.loads(request.body.decode()))
        post_data = json.loads(request.body.decode())
        # print(post_data["phone_number"])

        date_from = post_data["date_from"]
        date_to = post_data["date_to"]
        vehicle = post_data["vehicle"]

        date_from = datetime.strptime(
            date_from, "%d-%m-%Y").date()

        date_to = datetime.strptime(
            date_to, "%d-%m-%Y").date()

        try:

            print(get_profit_loss_array_by_date(
                user, vehicle, date_from, date_to))

            if get_profit_loss_array_by_date(user, vehicle, date_from, date_to):
                result = {
                    "status_code": 200,
                    "message": "",
                    "data": get_profit_loss_array_by_date(user, vehicle, date_from, date_to),
                }

                return JsonResponse(result)
            else:
                result = {
                    "status_code": 400,
                    "message": ""
                }

                return JsonResponse(result)

        except Exception as e:
            print("----", e)
            result = {
                "status_code": 400,
                "message": "Error: Unable to read data."
            }
            return JsonResponse(result)

    context = {
        "company_name": company_profile_obj.company_name,
        "company_vehicle_obj": company_vehicle_obj,
        "type_of_expenditure_obj": type_of_expenditure_obj,
        "pl_array": get_profit_loss_array(user)
    }
    return render(request, "profit_loss.html", context)
