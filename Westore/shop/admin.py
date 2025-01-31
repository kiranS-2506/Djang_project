from django.contrib import admin
from .models import *

# Register your models here.
class CategoryInfo(admin.ModelAdmin):
    list_display = ["name"]
class Productinfo(admin.ModelAdmin):
    list_display = ["name","price","category"]


admin.site.register(product,Productinfo)
admin.site.register(Category,CategoryInfo)

