from django.urls import path

from .Views.index import Index
from .Views.signin import Signin
from .Views.signup import Signup
from .Views.logout import Logout
from .Views.cart_details import Cart_details

urlpatterns = [
    path('', Index.as_view(), name='IndexPage'),
    path('signin', Signin.as_view(),name='Sign_User'),
    path('signup', Signup.as_view()),
    path('logout', Logout.as_view()),
    path('cart', Cart_details.as_view(),name="Cart"),
]
