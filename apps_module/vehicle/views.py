from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from apps_module.vehicle.forms import VehicleForm
from apps_module.company.models import CompanyProfile
from .models import Vehicle

# Create your views here.


def vehicle(request):
    user = request.user
    company_profile_obj = CompanyProfile.objects.get(user=user)
    vehicle_obj = Vehicle.objects.filter(
        company=company_profile_obj)
    vehicle_form = VehicleForm(request.POST or None)

    # form = VehicleTypeForm(request.POST or None)

    if request.method == "POST":
        print("=========", request.POST)
        if vehicle_form.is_valid():
            post_data = request.POST
            try:

                vehicle_code = vehicle_form.cleaned_data['vehicle_code']
                vehicle_registration_no = vehicle_form.cleaned_data['vehicle_registration_no']
                vehicle_manufacturer = vehicle_form.cleaned_data['vehicle_manufacturer']
                vehicle_type = vehicle_form.cleaned_data['vehicle_type']
                vehicle_model = vehicle_form.cleaned_data['vehicle_model']
                vehicle_color = vehicle_form.cleaned_data['vehicle_color']
                vehicle_fuel_type = vehicle_form.cleaned_data['vehicle_fuel_type']
                vehicle_purpose = vehicle_form.cleaned_data['vehicle_purpose']
                vehicle_status = vehicle_form.cleaned_data['vehicle_status']
                vehicle_passenger_limit = vehicle_form.cleaned_data['vehicle_passenger_limit']
                vehicle_cargo_limit = vehicle_form.cleaned_data['vehicle_cargo_limit']

                Vehicle(company=company_profile_obj,
                        vehicle_code=vehicle_code,
                        vehicle_registration_no=vehicle_registration_no,
                        vehicle_manufacturer=vehicle_manufacturer,
                        vehicle_type=vehicle_type,
                        vehicle_model=vehicle_model,
                        vehicle_color=vehicle_color,
                        vehicle_fuel_type=vehicle_fuel_type,
                        vehicle_purpose=vehicle_purpose,
                        vehicle_status=vehicle_status,
                        vehicle_passenger_limit=vehicle_passenger_limit,
                        vehicle_cargo_limit=vehicle_cargo_limit,
                        ).save()
            except Exception as e:
                print(e)

            print("success")
        return HttpResponseRedirect('/vehicle')

    context = {
        "company_profile_obj": company_profile_obj,
        "vehicle_form": vehicle_form,
        "vehicle_obj": vehicle_obj,
    }
    return render(request, 'vehicle.html', context)


def edit_vehicle(request, vid):
    user = request.user
    company_profile_obj = CompanyProfile.objects.get(user=user)
    vehicle_obj = Vehicle.objects.filter(
        company=company_profile_obj)
    instance = get_object_or_404(Vehicle, id=vid)
    edit_vehicle_form = VehicleForm(request.POST or None, instance=instance)

    # form = VehicleTypeForm(request.POST or None)
    print("----------------------------")

    if request.method == "POST":
        print("XXXXXXXXXXXX")

        print(request.POST)
        if edit_vehicle_form.is_valid():
            try:

                vehicle_code = edit_vehicle_form.cleaned_data['vehicle_code']
                vehicle_registration_no = edit_vehicle_form.cleaned_data['vehicle_registration_no']
                vehicle_manufacturer = edit_vehicle_form.cleaned_data['vehicle_manufacturer']
                vehicle_type = edit_vehicle_form.cleaned_data['vehicle_type']
                vehicle_model = edit_vehicle_form.cleaned_data['vehicle_model']
                vehicle_color = edit_vehicle_form.cleaned_data['vehicle_color']
                vehicle_fuel_type = edit_vehicle_form.cleaned_data['vehicle_fuel_type']
                vehicle_purpose = edit_vehicle_form.cleaned_data['vehicle_purpose']
                vehicle_status = edit_vehicle_form.cleaned_data['vehicle_status']
                vehicle_passenger_limit = edit_vehicle_form.cleaned_data['vehicle_passenger_limit']
                vehicle_cargo_limit = edit_vehicle_form.cleaned_data['vehicle_cargo_limit']

                Vehicle.objects.filter(id=vid).update(company=company_profile_obj,
                                                      vehicle_code=vehicle_code,
                                                      vehicle_registration_no=vehicle_registration_no,
                                                      vehicle_manufacturer=vehicle_manufacturer,
                                                      vehicle_type=vehicle_type,
                                                      vehicle_model=vehicle_model,
                                                      vehicle_color=vehicle_color,
                                                      vehicle_fuel_type=vehicle_fuel_type,
                                                      vehicle_purpose=vehicle_purpose,
                                                      vehicle_status=vehicle_status,
                                                      vehicle_passenger_limit=vehicle_passenger_limit,
                                                      vehicle_cargo_limit=vehicle_cargo_limit,
                                                      )
            except Exception as e:
                raise e
                print(e)

            print("--updated")
        return HttpResponseRedirect('/vehicle')

    context = {
        "vehicle_form": edit_vehicle_form,
        "vehicle_obj": vehicle_obj,
    }
    return render(request, 'vehicle_edit.html', context)


def delete_vehicle(request):
    post_obj = request.POST.getlist("items")
    print("post_obj")
    if request.method == "POST":
        for item in post_obj:
            # print emails
            Vehicle.objects.get(id=item).delete()
            print('deleted')
        return HttpResponseRedirect('/vehicle')
