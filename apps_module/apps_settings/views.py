from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from apps_module.company.models import CompanyProfile
from apps_module.apps_settings.models import (Position, Department, Employee, CarType)
from apps_module.apps_settings.forms import (PositionForm, DepartmentForm, EmployeeForm, CarTypeForm)

# Create your views here.


#  =============  position ============
def position(request):
    user = request.user
    company_profile_obj = CompanyProfile.objects.get(user=user)
    obj = Position.objects.filter(
        company=company_profile_obj)
    form = PositionForm(request.POST or None)

    if request.method == "POST":
        print(request.POST)
        if form.is_valid():
            post_data = request.POST
            try:
                position_name = form.cleaned_data['position_name']

                Position(company=company_profile_obj,
                        position_name=position_name
                        ).save()
            except Exception as e:
                print(e)

            print("success")
        return HttpResponseRedirect('/position')

    context = {
        "form": form,
        "obj": obj,
    }
    return render(request, 'position.html', context)


def edit_position(request, id):
    user = request.user
    company_profile_obj = CompanyProfile.objects.get(user=user)
    obj = Position.objects.filter(company=company_profile_obj)
    instance = get_object_or_404(Position, id=id)

    print("------ ", instance)

    form = PositionForm(request.POST or None, instance=instance)

    if request.method == "POST":
        print(request.POST)
        if form.is_valid():
            post_data = request.POST
            try:
                position_name = form.cleaned_data['position_name']

                Position.objects.filter(id=id).update(
                        position_name=position_name
                        )
            except Exception as e:
                print(e)

            print("success")
        return HttpResponseRedirect('/position')

    context = {
        "form": form,
        "obj": obj,
    }
    return render(request, 'position_edit.html', context)



#  =============  department ============
def department(request):
    user = request.user
    company_profile_obj = CompanyProfile.objects.get(user=user)
    obj = Department.objects.filter(
        company=company_profile_obj)
    form = DepartmentForm(request.POST or None)

    if request.method == "POST":
        print(request.POST)
        if form.is_valid():
            post_data = request.POST
            try:
                department_name = form.cleaned_data['department_name']

                Department(company=company_profile_obj,
                        department_name=department_name
                        ).save()
            except Exception as e:
                print(e)

            print("success")
        return HttpResponseRedirect('/department')

    context = {
        "form": form,
        "obj": obj,
    }
    return render(request, 'department.html', context)


def edit_department(request, id):
    user = request.user
    company_profile_obj = CompanyProfile.objects.get(user=user)
    obj = Department.objects.filter(company=company_profile_obj)
    instance = get_object_or_404(Department, id=id)

    print("------ ", instance)

    form = DepartmentForm(request.POST or None, instance=instance)

    if request.method == "POST":
        print(request.POST)
        if form.is_valid():
            post_data = request.POST
            try:
                department_name = form.cleaned_data['department_name']

                Department.objects.filter(id=id).update(
                        department_name=department_name
                        )
            except Exception as e:
                print(e)

            print("success")
        return HttpResponseRedirect('/department')

    context = {
        "form": form,
        "obj": obj,
    }
    return render(request, 'department_edit.html', context)


# =================================================================


def employee(request):
    user = request.user
    company_profile_obj = CompanyProfile.objects.get(user=user)
    employee_obj = Employee.objects.filter(
        company=company_profile_obj)
    employee_form = EmployeeForm(request.POST or None)

    # form = VehicleTypeForm(request.POST or None)

    if request.method == "POST":
        # print(request.POST)
        if employee_form.is_valid():
            # post_data = request.POST
            print(request.POST)
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
                department = employee_form.cleaned_data['department']

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
                        department=department,

                        ).save()
                
            except Exception as e:
                print(e)
                raise e

            print("success")
        return HttpResponseRedirect('/employee')

    context = {
        "form": employee_form,
        "obj": employee_obj,
    }
    return render(request, 'employee.html', context)


def edit_employee(request, id):
    user = request.user
    company_profile_obj = CompanyProfile.objects.get(user=user)
    employee_obj = Employee.objects.filter(
        company=company_profile_obj)
    instance = get_object_or_404(Employee, id=id)
    edit_employee_form = EmployeeForm(request.POST or None, instance=instance)

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
                department = edit_employee_form.cleaned_data['department']

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
                         department=department,
                         )
            except Exception as e:
                print(e)

            print("--updated--")
        return HttpResponseRedirect('/employee')

    context = {
        "form": edit_employee_form,
        "obj": employee_obj,
    }
    return render(request, 'employee_edit.html', context)







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


# def delete_employee(request):
#     post_obj = request.POST.getlist("items")
#     print("post_obj")
#     if request.method == "POST":
#         for item in post_obj:
#             # print emails
#             Employee.objects.get(id=item).delete()
#             print('deleted')
#         return HttpResponseRedirect('/employee')


def cartype(request):
    user = request.user
    company_profile_obj = CompanyProfile.objects.get(user=user)
    obj = CarType.objects.filter(
        company=company_profile_obj)
    form = CarTypeForm(request.POST or None)

    if request.method == "POST":
        print(request.POST)
        if form.is_valid():
            post_data = request.POST
            try:
                car_type = form.cleaned_data['car_type']

                CarType(company=company_profile_obj,
                        car_type=car_type
                        ).save()
            except Exception as e:
                print(e)

            print("success")
        return HttpResponseRedirect('/cartype')

    context = {
        "form": form,
        "obj": obj,
    }
    return render(request, 'car_type.html', context)


def edit_cartype(request, id):
    user = request.user
    company_profile_obj = CompanyProfile.objects.get(user=user)
    obj = CarType.objects.filter(company=company_profile_obj)
    instance = get_object_or_404(CarType, id=id)

    print("------ ", instance)

    form = CarTypeForm(request.POST or None, instance=instance)

    if request.method == "POST":
        print(request.POST)
        if form.is_valid():
            post_data = request.POST
            try:
                car_type = form.cleaned_data['car_type']

                CarType.objects.filter(id=id).update(
                        car_type=car_type
                        )
            except Exception as e:
                print(e)

            print("success")
        return HttpResponseRedirect('/cartype')

    context = {
        "form": form,
        "obj": obj,
    }
    return render(request, 'car_type_edit.html', context)
