from django.shortcuts import render
from django.http import HttpResponse
from shop.models import product,Category

# Create your views here.
def home(request):
    qs = product.objects.all()
    categories = Category.objects.all()
    response = render(request,"shop/index.html",context={"qs":qs,'cate':categories})
    
    return response
