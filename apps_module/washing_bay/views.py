from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from apps_module.company.models import CompanyProfile
from .models import WashingBayPrices, WashingBaySales
from .forms import WashingBayPricesForm, WashingBaySalesForm

# Create your views here.


def washing_bay_prices(request):
    user = request.user
    company_profile_obj = CompanyProfile.objects.get(user=user)
    bay_prices_obj = WashingBayPrices.objects.filter(
        company=company_profile_obj)
    bay_price_form = WashingBayPricesForm(request.POST or None)

    if request.method == "POST":
        if bay_price_form.is_valid():
            print(request.POST)
            try:
                car_type = bay_price_form.cleaned_data['car_type']
                body = bay_price_form.cleaned_data['body']
                engine = bay_price_form.cleaned_data['engine']
                under = bay_price_form.cleaned_data['under']
                inside = bay_price_form.cleaned_data['inside']
                blowing = bay_price_form.cleaned_data['blowing']
                hoover = bay_price_form.cleaned_data['hoover']

                WashingBayPrices(company=company_profile_obj,
                                 car_type=car_type,
                                 body=body,
                                 engine=engine,
                                 under=under,
                                 inside=inside,
                                 blowing=blowing,
                                 hoover=hoover,
                                 ).save()

            except Exception as e:
                print(e)
                raise e

            print("success")
        return HttpResponseRedirect('/washing_bay_prices')

    context = {
        "form": bay_price_form,
        "obj": bay_prices_obj,
    }
    return render(request, 'washing_bay_prices.html', context)


@login_required()
def edit_washing_bay_prices(request, id):
    user = request.user
    company_profile_obj = CompanyProfile.objects.get(user=user)
    bay_prices_obj = WashingBayPrices.objects.filter(
        company=company_profile_obj)

    instance = get_object_or_404(WashingBayPrices, id=id)

    bay_price_form = WashingBayPricesForm(
        request.POST or None, instance=instance)

    if request.method == "POST":
        if bay_price_form.is_valid():
            print(request.POST)
            try:
                car_type = bay_price_form.cleaned_data['car_type']
                body = bay_price_form.cleaned_data['body']
                engine = bay_price_form.cleaned_data['engine']
                under = bay_price_form.cleaned_data['under']
                inside = bay_price_form.cleaned_data['inside']
                blowing = bay_price_form.cleaned_data['blowing']
                hoover = bay_price_form.cleaned_data['hoover']

                WashingBayPrices.objects.filter(id=id).update(company=company_profile_obj,
                                                              car_type=car_type,
                                                              body=body,
                                                              engine=engine,
                                                              under=under,
                                                              inside=inside,
                                                              blowing=blowing,
                                                              hoover=hoover,
                                                              )

            except Exception as e:
                print(e)
                raise e

            print("success")
        return HttpResponseRedirect('/washing_bay_prices')

    context = {
        "form": bay_price_form,
        "obj": bay_prices_obj,
    }
    return render(request, 'washing_bay_prices.html', context)


def washing_bay_sales(request):
    user = request.user
    company_profile_obj = CompanyProfile.objects.get(user=user)
    bay_sales_obj = WashingBaySales.objects.filter(
        company=company_profile_obj)
    bay_sales_form = WashingBaySalesForm(request.POST or None)

    if request.method == "POST":
        if bay_sales_form.is_valid():
            print(request.POST)
            try:
                date = bay_sales_form.cleaned_data['date']
                car_type = bay_sales_form.cleaned_data['car_type']
                registration_number = bay_sales_form.cleaned_data['registration_number']
                body = bay_sales_form.cleaned_data['body']
                engine = bay_sales_form.cleaned_data['engine']
                under = bay_sales_form.cleaned_data['under']
                inside = bay_sales_form.cleaned_data['inside']
                blowing = bay_sales_form.cleaned_data['blowing']
                hoover = bay_sales_form.cleaned_data['hoover']
                amount = bay_sales_form.cleaned_data['amount']
                attendant = bay_sales_form.cleaned_data['attendant']

                WashingBaySales(company=company_profile_obj,
                                date=date,
                                registration_number=registration_number,
                                car_type=car_type,
                                body=body,
                                engine=engine,
                                under=under,
                                inside=inside,
                                blowing=blowing,
                                hoover=hoover,
                                amount=amount,
                                attendant=attendant,
                                ).save()

            except Exception as e:
                print(e)
                raise e

            print("success")
        return HttpResponseRedirect('/washing_bay_sales')

    context = {
        "form": bay_sales_form,
        "obj": bay_sales_obj,
    }
    return render(request, 'washing_bay_sales.html', context)


def edit_washing_bay_sales(request, id):
    user = request.user
    company_profile_obj = CompanyProfile.objects.get(user=user)
    bay_sales_obj = WashingBaySales.objects.filter(
        company=company_profile_obj)
    instance = get_object_or_404(WashingBaySales, id=id)
    bay_sales_form = WashingBaySalesForm(
        request.POST or None, instance=instance)

    if request.method == "POST":
        if bay_sales_form.is_valid():
            print(request.POST)
            try:
                date = bay_sales_form.cleaned_data['date']
                car_type = bay_sales_form.cleaned_data['car_type']
                registration_number = bay_sales_form.cleaned_data['registration_number']
                body = bay_sales_form.cleaned_data['body']
                engine = bay_sales_form.cleaned_data['engine']
                under = bay_sales_form.cleaned_data['under']
                inside = bay_sales_form.cleaned_data['inside']
                blowing = bay_sales_form.cleaned_data['blowing']
                hoover = bay_sales_form.cleaned_data['hoover']
                amount = bay_sales_form.cleaned_data['amount']
                attendant = bay_sales_form.cleaned_data['attendant']

                WashingBaySales.objects.filter(id=id).update(company=company_profile_obj,
                                                             date=date,
                                                             registration_number=registration_number,
                                                             car_type=car_type,
                                                             body=body,
                                                             engine=engine,
                                                             under=under,
                                                             inside=inside,
                                                             blowing=blowing,
                                                             hoover=hoover,
                                                             amount=amount,
                                                             attendant=attendant,
                                                             )
            except Exception as e:
                print(e)
                raise e

            print("success")
        return HttpResponseRedirect('/washing_bay_sales')

    context = {
        "form": bay_sales_form,
        "obj": bay_sales_obj,
    }
    return render(request, 'washing_bay_sales_edit.html', context)


def delete_washing_bay_sales(request, id):
    WashingBaySales.objects.get(id=id).delete()
    print('deleted')
    return HttpResponseRedirect('/washing_bay_sales')