from django.contrib import admin
from .models import *

# Register your models here.
class CategoryInfo(admin.ModelAdmin):
    list_display = ["name"]
class Productinfo(admin.ModelAdmin):
    list_display = ["name","price","category"]
class customerinfo(admin.ModelAdmin):
    list_display=["User_name","email","mobile","password"]
class cartinfo(admin.ModelAdmin):
     list_display = ["get_customer_name", "get_product_name", "quantity"]

    # Method to get the customer User_name
     def get_customer_name(self, obj):
        return obj.customer.User_name
    
    # Method to get the product name
     def get_product_name(self, obj):
        return obj.product.name

admin.site.register(product,Productinfo)
admin.site.register(Category,CategoryInfo)
admin.site.register(Customer,customerinfo)
admin.site.register(Cart,cartinfo)

