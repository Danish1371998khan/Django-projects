from django.views import View
from django.shortcuts import redirect

class Logout(View):
    def get(self,request):
        if request.session.get('user_email'):
            request.session.pop('user_email')
            request.session.pop('cart')
        return redirect('Sign_User')
