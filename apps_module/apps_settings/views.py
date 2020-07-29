from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .forms import (VehicleTypeForm,
                    VehiclePurposeForm,
                    EmployeeForm)
from apps_module.company.models import CompanyProfile
from apps_module.apps_settings.models import (VehicleType,
                                              VehicleFuelType,
                                              VehiclePurpose,
                                              VehicleStatus,
                                              Employee)
# Create your views here.


def vehicle_settings(request):
    user = request.user
    company_profile_obj = CompanyProfile.objects.get(user=user)
    obj = VehicleType.objects.filter(company=company_profile_obj)
    vehicle_purpose_obj = VehiclePurpose.objects.filter(
        company=company_profile_obj)

    form = VehicleTypeForm(request.POST or None)
    vehicle_purpose_form = VehiclePurposeForm(request.POST or None)

    if request.method == "POST":
        print(request.POST)
        if form.is_valid():
            post_data = request.POST
            vehicle_type = form.cleaned_data['vehicle_type']

            print(vehicle_type)
            VehicleType(company=company_profile_obj,
                        vehicle_type=vehicle_type).save()

            print("success")

    context = {
        "form": form,
        "obj": obj,
        "vehicle_purpose_form": vehicle_purpose_form,
        "vehicle_purpose_obj": vehicle_purpose_obj,
    }
    return render(request, 'vehicle_settings.html', context)


def add_vehicle_type(request):
    user = request.user
    company_profile_obj = CompanyProfile.objects.get(user=user)
    obj = VehicleType.objects.filter(company=company_profile_obj)
    form = VehicleTypeForm(request.POST or None)

    if request.method == "POST":
        print(request.POST)
        if form.is_valid():
            post_data = request.POST
            vehicle_type = form.cleaned_data['vehicle_type']

            print(vehicle_type)
            VehicleType(company=company_profile_obj,
                        vehicle_type=vehicle_type).save()

            print("success")
        return HttpResponseRedirect('/vehicle_settings')

    context = {
        "form": form,
        "obj": obj,
    }
    return render(request, 'vehicle_settings.html', context)


def edit_vehicle_type(request, pid):
    user = request.user
    instance = get_object_or_404(VehicleType, id=pid)
    company_profile_obj = CompanyProfile.objects.get(user=user)
    obj = VehicleType.objects.filter(company=company_profile_obj)
    vehicle_purpose_obj = VehiclePurpose.objects.filter(
        company=company_profile_obj)
    edit_form = VehicleTypeForm(request.POST or None, instance=instance)

    if request.method == "POST":
        print(request.POST)
        if edit_form.is_valid():
            post_data = request.POST
            vehicle_type = edit_form.cleaned_data['vehicle_type']

            print(vehicle_type)
            VehicleType.objects.filter(id=pid).update(
                vehicle_type=vehicle_type)

            print("---updated---")
            return HttpResponseRedirect('/vehicle_settings')

    context = {
        "form": edit_form,
        "obj": obj,
        "vehicle_purpose_obj": vehicle_purpose_obj,

    }
    return render(request, 'vehicle_settings.html', context)


def delete_vehicle_type(request):
    post_obj = request.POST.getlist("items")
    print("post_obj")
    if request.method == "POST":
        for item in post_obj:
            # print emails
            VehicleType.objects.get(id=item).delete()
            print('deleted')
        return HttpResponseRedirect('/vehicle_settings')


# ================================================================


def add_vehicle_purpose(request):
    user = request.user
    company_profile_obj = CompanyProfile.objects.get(user=user)
    vehicle_purpose_obj = VehiclePurpose.objects.filter(
        company=company_profile_obj)
    vehicle_purpose_form = VehiclePurposeForm(request.POST or None)

    form = VehicleTypeForm(request.POST or None)

    if request.method == "POST":
        print(request.POST)
        if vehicle_purpose_form.is_valid():
            post_data = request.POST
            purpose_name = vehicle_purpose_form.cleaned_data['purpose_name']

            print(purpose_name)
            VehiclePurpose(company=company_profile_obj,
                           purpose_name=purpose_name).save()

            print("success")
        return HttpResponseRedirect('/vehicle_settings')

    context = {
        "vehicle_purpose_form": vehicle_purpose_form,
        "vehicle_purpose_obj": vehicle_purpose_obj,
    }
    return render(request, 'vehicle_settings.html', context)


def edit_vehicle_purpose(request, id):
    user = request.user
    instance = get_object_or_404(VehiclePurpose, id=id)
    company_profile_obj = CompanyProfile.objects.get(user=user)
    obj = VehicleType.objects.filter(company=company_profile_obj)
    vehicle_purpose_obj = VehiclePurpose.objects.filter(
        company=company_profile_obj)
    edit_vehicle_purpose_form = VehiclePurposeForm(
        request.POST or None, instance=instance)

    if request.method == "POST":
        print(request.POST)
        if edit_vehicle_purpose_form.is_valid():
            post_data = request.POST
            purpose_name = edit_vehicle_purpose_form.cleaned_data['purpose_name']

            print(purpose_name)
            VehiclePurpose.objects.filter(id=id).update(
                purpose_name=purpose_name)

            print("---updated---")
            return HttpResponseRedirect('/vehicle_settings')

    context = {

        "obj": obj,
        "vehicle_purpose_form": edit_vehicle_purpose_form,
        "vehicle_purpose_obj": vehicle_purpose_obj,
    }
    return render(request, 'vehicle_settings.html', context)


def delete_vehicle_purpose(request):
    post_obj = request.POST.getlist("items")
    print("post_obj")
    if request.method == "POST":
        for item in post_obj:
            # print emails
            VehiclePurpose.objects.get(id=item).delete()
            print('deleted')
        return HttpResponseRedirect('/vehicle_settings')


# =================================================================


def employee(request):
    user = request.user
    company_profile_obj = CompanyProfile.objects.get(user=user)
    employee_obj = Employee.objects.filter(
        company=company_profile_obj)
    employee_form = EmployeeForm(request.POST or None)

    # form = VehicleTypeForm(request.POST or None)

    if request.method == "POST":
        print(request.POST)
        if employee_form.is_valid():
            post_data = request.POST
            try:
                employee_id = employee_form.cleaned_data['employee_id']
                first_name = employee_form.cleaned_data['first_name']
                last_name = employee_form.cleaned_data['last_name']
                date_of_birth = employee_form.cleaned_data['date_of_birth']
                gender = employee_form.cleaned_data['gender']
                location = employee_form.cleaned_data['location']
                phone_number_1 = employee_form.cleaned_data['phone_number_1']
                phone_number_2 = employee_form.cleaned_data['phone_number_2']
                position = employee_form.cleaned_data['position']

                Employee(company=company_profile_obj,
                        employee_id=employee_id,
                        first_name=first_name,
                        last_name=last_name,
                        date_of_birth=date_of_birth,
                        gender=gender,
                        location=location,
                        phone_number_1=phone_number_1,
                        phone_number_2=phone_number_2,
                        position=position,
                        ).save()
            except Exception as e:
                print(e)

            print("success")
        return HttpResponseRedirect('/employee')

    context = {
        "employee_form": employee_form,
        "employee_obj": employee_obj,
    }
    return render(request, 'employee_settings.html', context)


def edit_employee(request, id):
    user = request.user
    company_profile_obj = CompanyProfile.objects.get(user=user)
    employee_obj = Employee.objects.filter(
        company=company_profile_obj)
    instance = get_object_or_404(Employee, id=id)
    edit_employee_form = EmployeeForm(request.POST or None, instance)

    # form = VehicleTypeForm(request.POST or None)

    if request.method == "POST":
        print(request.POST)
        if edit_employee_form.is_valid():
            post_data = request.POST
            try:
                employee_id = edit_employee_form.cleaned_data['employee_id']
                first_name = edit_employee_form.cleaned_data['first_name']
                last_name = edit_employee_form.cleaned_data['last_name']
                date_of_birth = edit_employee_form.cleaned_data['date_of_birth']
                gender = edit_employee_form.cleaned_data['gender']
                location = edit_employee_form.cleaned_data['location']
                phone_number_1 = edit_employee_form.cleaned_data['phone_number_1']
                phone_number_2 = edit_employee_form.cleaned_data['phone_number_2']
                position = edit_employee_form.cleaned_data['position']

                Employee.objects.filter(id=id).update(company=company_profile_obj,
                         employee_id=employee_id,
                         first_name=first_name,
                         last_name=last_name,
                         date_of_birth=date_of_birth,
                         gender=gender,
                         location=location,
                         phone_number_1=phone_number_1,
                         phone_number_2=phone_number_2,
                         position=position,
                         )
            except Exception as e:
                print(e)

            print("--updated--")
        return HttpResponseRedirect('/employee')

    context = {
        "employee_form": edit_employee_form,
        "employee_obj": employee_obj,
    }
    return render(request, 'employee_settings.html', context)



# def edit_employee(request, id):
#     user = request.user
#     instance = get_object_or_404(VehiclePurpose, id=id)
#     company_profile_obj = CompanyProfile.objects.get(user=user)
#     obj = VehicleType.objects.filter(company=company_profile_obj)
#     vehicle_purpose_obj = VehiclePurpose.objects.filter(
#         company=company_profile_obj)
#     edit_vehicle_purpose_form = VehiclePurposeForm(
#         request.POST or None, instance=instance)

#     if request.method == "POST":
#         print(request.POST)
#         if edit_vehicle_purpose_form.is_valid():
#             post_data = request.POST
#             purpose_name = edit_vehicle_purpose_form.cleaned_data['purpose_name']

#             print(purpose_name)
#             VehiclePurpose.objects.filter(id=id).update(
#                 purpose_name=purpose_name)

#             print("---updated---")
#             return HttpResponseRedirect('/vehicle_settings')

#     context = {

#         "obj": obj,
#         "vehicle_purpose_form": edit_vehicle_purpose_form,
#         "vehicle_purpose_obj": vehicle_purpose_obj,
#     }
#     return render(request, 'vehicle_settings.html', context)


def delete_employee(request):
    post_obj = request.POST.getlist("items")
    print("post_obj")
    if request.method == "POST":
        for item in post_obj:
            # print emails
            VehiclePurpose.objects.get(id=item).delete()
            print('deleted')
        return HttpResponseRedirect('/vehicle_settings')
