from django.shortcuts import render,redirect
from django.views import View
from Store.models.new_user import New_User
from django.contrib.auth.hashers import check_password


class Signin(View):

    def get(self, request):
        return render(request, 'Signin.html')

    def post(self, request):

        email = request.POST.get('email')
        password = request.POST.get('password')
        error_message = None
        if New_User.isExist(email):
            if check_password( password , New_User.get_user_by_email(email).password):

                user_email = request.session.get('user_email')
                user_email={'email':email}
                request.session['user_email']=user_email

                return redirect('IndexPage')
            else:
                error_message = 'Email or password invalid'
        else:
            error_message = 'Email or password invalid'

        data_dict = {'error':error_message , 'email':email}
        return render(request, 'Signin.html', data_dict)