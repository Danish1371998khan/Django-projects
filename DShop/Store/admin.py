from django.contrib import admin

from .models.category import Category
from .models.new_user import New_User
from .models.product import Product


class Admin_Site_Product_View(admin.ModelAdmin):
    list_display = [
        'brand', 'name', 'price', 'discription', 'category'
    ]


class Admin_Site_Category_View(admin.ModelAdmin):
    list_display = [
        'category'
    ]


class Admin_Site_New_User_Detalis(admin.ModelAdmin):
    list_display = [
        'first_name', 'last_name', 'email', 'phone_no', 'password'
    ]


admin.site.register(Product, Admin_Site_Product_View)
admin.site.register(Category, Admin_Site_Category_View)
admin.site.register(New_User, Admin_Site_New_User_Detalis)
