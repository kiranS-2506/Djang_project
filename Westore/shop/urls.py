from django.urls import path
from shop.views import *

urlpatterns = [
    path("",home, name="home"),
    path('category/',getcatgories, name='category'),
    path('signup/',Signup, name='signup'),
    path("login/",SignIn, name='login'),
    path("addToCart/<int:product_id>",addToCart, name="addToCart"),
    path("viewcart/",view_cart, name='viewcart'),
    path('update_quantity/<int:item_id>',update_quantity, name='update_quantity'),
    path('remove_item/<int:item_id>',remove_item, name='remove_item'),
    path('place_order',place_order, name='place_order'),
    path("logout/",logout, name='logout'),
]
