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
# Create your views here.

# from api.serializers import (
#     UserAdminSerializer,
#     PersonalProfileSerializer,
#     AccountProfileSerializer,
#     NetworkProfileSerializer,
#     UserLoginSerializer,

# )

# from userapp.models import (
#     PersonalProfile,
#     AccountProfile,
#     NetworkProfile,
#     Complaint,
#     PaymentTransaction,
#     RegistrationPaymentInfo,
#     PasswordVerification,
#     BenefitRequest

# )

# from settingsapp.models import (ContactSettings, FeeSettings, LevelSettings)

from validate_email import validate_email
# from lib.phone import get_phone_to_username, get_phone_number, phone_to_momo_format
# from lib.RandomTokenGenerator import RandomTokenGenerator
# from lib.pyramid_engine import get_progress_level, check_current_level
# from lib.sms import send_signUp_sms, send_password_pin_sms
# from lib.email import send_signUp_email, send_contact_email
# from lib.get_upline import get_upline

# import requests


def homepage(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/profit_loss")
    context = {}
    return render(request, "login.html", context)


# @csrf_exempt
# @django_logout
def login(request, *args, **kwargs):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/profit_loss")

    message = ""
    result = ""
    print("xxxxxx")

    if request.method == "POST":
        print(json.loads(request.body.decode()))
        post_data = json.loads(request.body.decode())
        # print(post_data["phone_number"])

        user_email = post_data["user_email"]
        password = post_data["password"]

        try:
            user_reg = authenticate(username=user_email, password=password)
            if user_reg is not None:
                if user_reg.is_active:
                    if user_reg.is_staff:

                        auth_login(request, user_reg)
                        print("user staff logged in")
                        result = {
                            "status_code": 200,
                            "message": message,
                            "next_url": "/backend_dashboard"
                        }
                        return JsonResponse(result)
                    else:
                        auth_login(request, user_reg)
                        print("user logged in")
                        result = {
                            "status_code": 200,
                            "message": message,
                            "next_page": "/profit_loss"
                        }
                        return JsonResponse(result)
            else:
                message = "User email or password is incorrect"
                result = {
                    "status_code": 400,
                    "message": message,
                }
            return JsonResponse(result)
        except Exception as e:
            raise e
            message = "Account does not exist, please register"
            result = {
                "status_code": 500,
                "message": message,
            }
            return JsonResponse(result)

    context = {}
    return render(request, "login.html", context)


def register(request, *args, **kwargs):
        # if request.user.is_staff:
        #     return HttpResponseRedirect("/backend_dashboard")

    if request.method == "POST":
        print(json.loads(request.body.decode()))
        post_data = json.loads(request.body.decode())
        # print(post_data["phone_number"])

        company_name = post_data["company_name"]

        first_name = post_data["first_name"]
        last_name = post_data["last_name"]
        u_email = post_data["email"]

        password = post_data["password"]

        if User.objects.filter(username=u_email).exists():
            print(u_email, "already exists")
            message = "Sorry, user already exists, please try again."
            data = {}
            result = {
                "status_code": 400,
                "message": message,
                "data": data,
            }
            return JsonResponse(result)

        if CompanyProfile.objects.filter(company_name=company_name).exists():
            print(company_name, "already exists")
            message = "Sorry, Company already exists, please try again."
            data = {}
            result = {
                "status_code": 400,
                "message": message,
                "data": data,
            }
            return JsonResponse(result)

        if len(u_email) > 0:
            is_valid = validate_email(str(u_email))
            print(is_valid)
            if is_valid == True:
                try:
                    user = User.objects.create_user(username=u_email, password=password,
                                                    first_name=first_name, last_name=last_name, email=u_email)
                    user.is_active = True

                    CompanyProfile.objects.create(
                        user=user, company_name=company_name)

                    user_reg = authenticate(
                        username=user.username, password=password)
                    if user_reg is not None:
                        if user_reg.is_active:
                            auth_login(request, user_reg)

                            print("user logged in")
                            message = ""
                            result = {
                                "status_code": 200,
                                "message": message,
                                "next_page": "/profit_loss",
                            }
                            return JsonResponse(result)
                            # return HttpResponseRedirect("/dashboard")
                        print("continue")

                except Exception as e:
                    print("error", e)
                    message = "User account not created, please contact Administrator"
                    result = {
                        "status_code": 500,
                        "message": message,
                    }
                    return JsonResponse(result)
            else:
                result = {
                    "status_code": 404,
                    "message": "Email address is invalid",
                }
                return JsonResponse(result)

        # verify payment, uplink and create user here

    context = {
        # "upline_id_url": upline_id_in_url.replace(""", ""),
    }
    # return Response(context)

    return render(request, "register.html", context)


def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")
    elif(request.user.is_staff):
        return HttpResponseRedirect("/backend_dashboard")
    else:
        pass


    user = request.user

    company_profile_obj = CompanyProfile.objects.get(user=user)
    
    context = {
        "company_name": company_profile_obj.company_name,
    }
    return render(request, "dashboard.html", context)




def company_profile(request, *args, **kwargs):
        # if request.user.is_staff:
        #     return HttpResponseRedirect("/backend_dashboard")

    if request.method == "POST":
        print(json.loads(request.body.decode()))
        post_data = json.loads(request.body.decode())

        user = request.user
        company_name = post_data["company_name"]
        address = post_data["address"]
        location = post_data["location"]
        phone_number = post_data["phone_number"]

        company_profile_obj = CompanyProfile.objects.create(user=user,
                                                            company_name=company_name,
                                                            company_address=address,
                                                            company_location=location,
                                                            company_phone_number=phone_number)
        if company_profile_obj:
            result = {
                "status_code": 200,
                "message": "",
                "next_page": "/profit_loss"
            }
        return JsonResponse(result)

    context = {
        # "upline_id_url": upline_id_in_url.replace(""", ""),
    }
    # return Response(context)

    return render(request, "company_profile.html", context)


# @login_required
def logout(request):
    if request.user is None:
        django_logout(request)
        return HttpResponseRedirect("/")
    elif request.user is not None:
        django_logout(request)
        return HttpResponseRedirect("/")


@csrf_exempt
def personalprofile(request):

    print(request.user)

    serializer = PersonalProfileSerializer

    context = {
        "serializer": serializer,
    }
    return render(request, "personal_profile.html", context)

# @csrf_exempt
# @login_required





@csrf_exempt
def howitworks(request):

    context = {}
    return render(request, "how-it-works.html", context)


# def dashProfileDetails(request):
#     user = request.user
#     print(user)
#     message = ""
#     accountmessage = ""
#     current_date = datetime.now()

#     # user_network_profile=NetworkProfile.objects.get(user=user)

#     try:
#         user_firstname = request.user.first_name
#         user_lastname = request.user.last_name
#         user_email = request.user.email

#         profile_obj = PersonalProfile.objects.get(user=user)

#         other_names = profile_obj.other_names
#         phone_number = str(profile_obj.phone_number)
#         date_of_birth = profile_obj.date_of_birth
#         occupation = profile_obj.occupation
#         country = str(profile_obj.country)
#         region = profile_obj.region
#         address = profile_obj.address
#         city = profile_obj.city
#         gender = profile_obj.gender
#         marital_status = profile_obj.marital_status
#         message = ""

#     except Exception as e:
#         print(e)
#         other_names = ""
#         phone_number = ""
#         date_of_birth = current_date
#         occupation = ""
#         country = ""
#         region = ""
#         address = ""
#         city = ""
#         gender = "---Select---"
#         marital_status = ""
#         message = "Update your profile"

#     # get user account details
#     try:
#         user_acc_details = AccountProfile.objects.get(user=user)

#         bank_account_name = user_acc_details.bank_account_name
#         bank_account_number = str(user_acc_details.bank_account_number)
#         bank_name = user_acc_details.bank_name
#         bank_branch = user_acc_details.bank_branch
#         mobile_money_number = str(user_acc_details.mobile_money_number)
#         mobile_money_name = user_acc_details.mobile_money_name
#         mobile_money_provider = user_acc_details.mobile_money_provider

#         accountmessage = ""

#     except Exception as e:
#         print("bank", e)
#         bank_account_name = ""
#         bank_account_number = ""
#         bank_name = ""
#         bank_branch = ""
#         mobile_money_number = ""
#         mobile_money_name = ""
#         mobile_money_provider = ""

#         accountmessage = "Update your Bank details"

#     # print(request.user.get_full_name())

#     if request.method == "POST":
#         post_data = json.loads(request.body.decode())
#         print(post_data)

#         try:
#             first_name = post_data["first_name"]
#             last_name = post_data["last_name"]
#             other_names = post_data["other_names"]
#             phone_number = post_data["phone_number"]
#             u_email = post_data["email"]
#             date_of_birth = post_data["date_of_birth"]

#             occupation = post_data["occupation"]
#             country = post_data["country"]
#             region = post_data["region"]

#             address = post_data["address"]
#             city = post_data["city"]
#             gender = post_data["gender"]
#             marital_status = post_data["marital_status"]

#             if len(u_email) > 0:
#                 is_valid = validate_email(str(u_email))
#                 print(is_valid)
#                 if is_valid == True:
#                     user_email = u_email
#                 else:
#                     result = {
#                         "status_code": 404,
#                         "message": "Email address is invalid",
#                     }
#                     return JsonResponse(result)
#             else:
#                 user_email = ""

#             new_user_obj = User.objects.filter(username=user).update(
#                 first_name=first_name, last_name=last_name, email=user_email)
#             print("user updated ", new_user_obj)

#             PersonalProfile.objects.filter(user=user).update(other_names=other_names,
#                                                              phone_number=get_phone_number(phone_number), date_of_birth=date_of_birth, occupation=occupation,
#                                                              country=country, region=region,
#                                                              address=address,
#                                                              city=city, gender=gender,
#                                                              marital_status=marital_status)

#             message = "Profile successfully updated."

#             result = {
#                 "status_code": 200,
#                 "message": message,
#             }
#             return JsonResponse(result)

#         except Exception as e:
#             # raise e
#             print("error", e)

#             result = {
#                 "status_code": 400,
#                 "message": "All fields are required",
#             }
#             return JsonResponse(result)

#     context = {
#         "user_fname": user_firstname,
#         "user_lastname": user_lastname,
#         "user_email": user_email,
#         # "user_network_id":user_network_profile.pyramid_guid,

#         "other_names": other_names,
#         "phone_number": get_phone_number(phone_number),
#         "date_of_birth": date_of_birth.strftime("%Y-%m-%d"),
#         "occupation": occupation,
#         "country": str(country),
#         "region": region,
#         "address": address,
#         "city": city,
#         "gender": gender,
#         "marital_status": marital_status,

#         "message": message,


#         "bank_account_name": bank_account_name,
#         "bank_account_number": str(bank_account_number),
#         "bank_name": bank_name,
#         "bank_branch": bank_branch,
#         "mobile_money_number": get_phone_number(mobile_money_number),
#         "mobile_money_name": mobile_money_name,
#         "mobile_money_provider": mobile_money_provider,


#         "accountmessage": accountmessage,
#     }
#     return render(request, "dash_personal_profile.html", context)


def updateAccountDetails(request):
    user = request.user
    message = ""
    print("u-", user)
    if request.method == "POST":
        post_data = json.loads(request.body.decode())
        print(post_data)

        bank_account_name = post_data["bank_account_name"]
        bank_account_number = post_data["bank_account_number"]
        bank_name = post_data["bank_name"]
        bank_branch = post_data["bank_branch"]
        mobile_money_number = post_data["mobile_money_number"]
        mobile_money_name = post_data["mobile_money_name"]
        mobile_money_provider = post_data["mobile_money_provider"]
    try:

        try:
            user_account_obj = AccountProfile.objects.get(user=user)
            if user_account_obj:
                AccountProfile.objects.filter(user=user).update(bank_account_name=bank_account_name,
                                                                bank_account_number=bank_account_number,
                                                                bank_name=bank_name, bank_branch=bank_branch,
                                                                mobile_money_number=get_phone_number(
                                                                    mobile_money_number),
                                                                mobile_money_name=mobile_money_name,
                                                                mobile_money_provider=mobile_money_provider)

                message = "Bank details successfully updated."
                result = {
                    "status_code": 200,
                    "message": message,
                }

                return JsonResponse(result)

        except Exception as e:
            print("error", e)
            AccountProfile.objects.create(user=user, bank_account_name=bank_account_name,
                                          bank_account_number=bank_account_number,
                                          bank_name=bank_name, bank_branch=bank_branch,
                                          mobile_money_number=get_phone_number(
                                              mobile_money_number),
                                          mobile_money_name=mobile_money_name,
                                          mobile_money_provider=mobile_money_provider)

            message = "Bank details created."
            result = {
                "status_code": 200,
                "message": message,
            }
            return JsonResponse(result)
            # raise e

    except Exception as e:
        print(e)
        message = "Bank details could not be updated."
        result = {
            "status_code": 400,
            "message": message,
        }
        return JsonResponse(result)
        # raise e


#


@csrf_exempt
def about_us(request):

    context = {}
    return render(request, "about_us.html", context)


# def contact_us(request):

#     if request.method == "POST":
#         post_data = json.loads(request.body.decode())
#         print("contact_us", post_data)
#         # contact_us {"fullname": "", "email": "", "subject": "", "message": "", "csrfmiddlewaretoken": "8f7uYxxcxVlNnBku97QKNzoxKw4iH9o6kBYg9zSGI78iWXoCadWHpPbeii4q4d5P"}

#         sender_name = post_data["fullname"]
#         sender_email = post_data["email"]
#         msg_subject = post_data["subject"]
#         msg = post_data["message"]
#         recaptcha_response = post_data["respuesta_recaptcha"]
#         website_email = settings.EMAIL_HOST_USER
#         email_receiver = settings.EMAIL_RECEIVER

#         try:
#             url = "https://www.google.com/recaptcha/api/siteverify"
#             values = {
#                 "secret": settings.GOOGLE_RECAPTCHA_SECRET_KEY,
#                 "response": recaptcha_response
#             }
#             data = urllib.parse.urlencode(values).encode()
#             req = urllib.request.Request(url, data=data)
#             response = urllib.request.urlopen(req)
#             feedback = json.loads(response.read().decode())

#             print("---", feedback)
#             if feedback["success"] == True:

#                 email_data = send_contact_email(
#                     msg_subject, sender_name, sender_email, msg)

#                 # print("Email data",email_data)

#                 message = "Thank you " + \
#                     str(sender_name).upper() + \
#                     " for contacting us. Your message has been successfully received."
#                 result = {
#                     "status_code": 200,
#                     "message": message,
#                 }
#                 return JsonResponse(result)
#             else:
#                 result = {
#                     "status_code": 401,
#                     "message": "Verify you are not a robot"
#                 }
#                 return JsonResponse(result)
#         except Exception as e:

#             print("error---", e)
#             message = "Sorry your message has not been received please try again"
#             result = {
#                 "status_code": 400,
#                 "message": message,
#             }
#             return JsonResponse(result)

#     context = {
#         "recapture_key": settings.GOOGLE_RECAPTCHA_SITE_KEY
#     }
#     return render(request, "contact_us.html", context)


# Create your views here.


def terms_conditions(request):
    return render(request, "terms_conditions.html", {})


def faqs(request):

    context = {}
    return render(request, "faqs.html", context)


# def forgot_password(request):
#     # user=request.user

#     # print(RandomTokenGenerator().generatePasswordPin())
#     if request.method == "POST":
#         post_data = json.loads(request.body.decode())
#         print("post data:", )
#         user_pin = post_data["user_pin"]

#         if User.objects.filter(username=user_pin).exists():
#             # send sms with pin, save pin and direct to verify page
#             user = User.objects.get(username=user_pin)
#             password_pin = RandomTokenGenerator().generatePasswordPin()
#             print(password_pin)

#             profile_obj = PersonalProfile.objects.get(user=user)
#             print("cell ", str(profile_obj.phone_number))
#             try:

#                 if PasswordVerification.objects.filter(user_pin__exact=user_pin).exists():
#                     PasswordVerification.objects.filter(
#                         user_pin__exact=user_pin).update(password_pin=password_pin)
#                     pass_pin_obj = PasswordVerification.objects.get(
#                         user_pin__exact=user_pin)
#                 else:
#                     pass_pin_obj = PasswordVerification.objects.create(
#                         user_pin=user_pin, password_pin=password_pin)

#                 print(pass_pin_obj)
#                 if pass_pin_obj:
#                     print(pass_pin_obj.password_pin)
#                     sms_data = send_password_pin_sms(
#                         user.first_name, profile_obj.phone_number, pass_pin_obj.password_pin)
#                     result = {
#                         "status_code": 200,
#                         "message": "",
#                         "next_url": "/verify_code"
#                     }
#                     return JsonResponse(result)

#             except Exception as e:
#                 print(e)
#                 raise e
#                 result = {
#                     "status_code": 400,
#                     "message": "Cannot change password, please try again or contact Administrator",
#                     # "next_url":"/verify_code"
#                 }
#                 return JsonResponse(result)

#         else:
#             result = {
#                 "status_code": 400,
#                 "message": "User email is invalid, Try again.",
#                 # "next_url":"/verify_digit"
#             }
#             return JsonResponse(result)

#     context = {}
#     return render(request, "forgot_password.html", context)


# def verify_code(request):

#     if request.method == "POST":
#         post_data = json.loads(request.body.decode())
#         print("post data:", )
#         vcode = post_data["vcode"]

#         if PasswordVerification.objects.filter(password_pin__exact=vcode).exists():
#             # send sms with pin, save pin and direct to verify page
#             pass_v_obj = PasswordVerification.objects.get(
#                 password_pin__exact=vcode)
#             user_pin = pass_v_obj.user_pin

#             print("yes")
#             result = {
#                 "status_code": 200,
#                 "message": "",
#                 "next_url": "/change_password/?q="+str(user_pin)+""
#             }
#             return JsonResponse(result)
#         else:
#             result = {
#                 "status_code": 400,
#                 "message": "Verification code is invalid, Try again.",
#                 # "next_url":"/verify_digit"
#             }
#             return JsonResponse(result)

#     context = {}
#     return render(request, "verify_code.html", context)


# def change_password(request, *args, **kwargs):
#     user_pin = request.GET.get("q")
#     print(user_pin)
#     if request.method == "POST":
#         post_data = json.loads(request.body.decode())
#         print("post data:", post_data)
#         post_user_pin = post_data["pin"]
#         new_password = post_data["new_password"]

#         if PasswordVerification.objects.filter(user_pin__exact=post_user_pin).exists():
#             # change password
#             user_obj = User.objects.get(username__exact=post_user_pin)
#             user_obj.set_password(new_password)
#             user_obj.save()

#             PasswordVerification.objects.filter(
#                 user_pin__exact=post_user_pin).delete()

#             if user_obj:
#                 print("yes")
#                 result = {
#                     "status_code": 200,
#                     "message": "",
#                     "next_url": "/login"
#                 }
#                 return JsonResponse(result)
#         else:
#             result = {
#                 "status_code": 400,
#                 "message": "Invalid Password request, Try again.",
#                 # "next_url":"/verify_digit"
#             }
#             return JsonResponse(result)

#     context = {
#         "user_pin": user_pin
#     }
#     return render(request, "change_password.html", context)
