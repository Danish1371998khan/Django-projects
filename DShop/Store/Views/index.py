from django.shortcuts import render,redirect
from django.views import View

from Store.models.category import Category
from Store.models.product import Product


class Index(View):
    def get(self, request):
        data_dict = {}
        cat_id = request.GET.get('category')
        data_dict['categories'] = Category.get_all_categories()
        if cat_id:
            data_dict['products'] = Product.get_products_by_productid(cat_id)
        else:
            data_dict['products'] = Product.get_all_products()
        return render(request, 'index.html', data_dict)

    def post(self,request):

        product_id=request.POST.get('clicked_product_id')
        cart = request.session.get('cart')
        if cart:
            if cart.get(product_id) and request.POST.get('remove'):
                cart[product_id]-=1
                if cart[product_id]==0:
                    cart.pop(product_id)
            elif cart.get(product_id):
                cart[product_id]+=1
            else:
                cart[product_id] = 1
        else:
            cart = {product_id:1}
        request.session['cart']=cart

        return redirect('IndexPage')