from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import View

from Store.models.new_user import New_User


class Signup(View):


    def get(self, request):
        return render(request, 'Signup.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        isvalid = Signup.verify_details(first_name, last_name, email, phone_no, password1, password2)

        if not isvalid:
            hashed_password = make_password(str(password1))
            obj1 = New_User()
            obj1.first_name = first_name
            obj1.last_name = last_name
            obj1.email = email
            obj1.phone_no = phone_no
            obj1.password = hashed_password

            obj1.add_profile_details()
            return redirect('IndexPage')
        else:
            populate_data = {
                'error': isvalid,
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone_no': phone_no
            }
        return render(request, 'Signup.html' , populate_data)

    @staticmethod
    def verify_details(first_name, last_name, email, phone_no, password1, password2):
        errormessage = None

        if (not first_name) and (not last_name) and (not phone_no) and (not password1) and (not password2):
            errormessage = "All fiels are required"
        elif not first_name:
            errormessage = 'First name is required'
        elif len(first_name) < 3:
            errormessage = 'First name cannot be less than 5 characters'
        elif not last_name:
            errormessage = 'Last name is required'
        elif len(last_name) < 2:
            errormessage = 'Last name cannot be less than 5 characters'
        elif New_User.isExist(email):
            errormessage = 'Email already taken'
        elif not phone_no:
            errormessage = 'Phone number required'
        elif len(phone_no) < 10:
            errormessage = 'Phone number must be greater than 9 characters'
        elif not password1:
            errormessage = 'Password cannot be empty'
        elif len(password1) != len(password2):
            errormessage = "Password doesn't match"

        return errormessage
