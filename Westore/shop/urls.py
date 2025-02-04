from django.urls import path
from shop.views import *

urlpatterns = [
    path("",home, name="home"),
    path('category/',getcatgories, name='category'),
    path('signup/',Signup),
    path("login/",SignIn, name='login'),
    path("addToCart/<int:product_id>",addToCart, name="addToCart")
]
