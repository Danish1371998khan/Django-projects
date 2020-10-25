from django.views import View
from django.shortcuts import render,redirect
from Store.models.product import Product

class Cart_details(View):
    def get(self,request):

        product_details = {}

        if request.session.get('cart'):
            keys = list(request.session.get('cart').keys())
            products = Product.get_products_by_id_list(keys)

            product_details = {'products': products}
        else:
            print("Cart is empty")

        return render(request,'cart_details.html',product_details)