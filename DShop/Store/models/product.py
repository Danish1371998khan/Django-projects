from django.db import models

from .category import Category


class Product(models.Model):
    brand = models.CharField(max_length=50, default='Gucci')
    image = models.ImageField(upload_to='com/danish/', default=1)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    discription = models.CharField(max_length=1000, null=True, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_products_by_productid(productID):
        return Product.objects.filter(category=productID)

    @staticmethod
    def get_products_by_id_list(ides):
        return Product.objects.filter(id__in=ides)