from django.shortcuts import render,redirect
from django.http import HttpResponse
from shop.models import product,Category,Customer,Cart
import re
from django.db.models import Q
# Create your views here.

def home(request):
    cname = request.session.get('cname',"")
    qs = product.objects.all()
    categories = Category.objects.all()
    response = render(request,"shop/index.html",context={"qs":qs,'cate':categories,'cname':cname})
    
    return response

def getcatgories(request):
    catg_id = request.GET.get('cat_id')
    cname = request.session.get('cname',"")
    categories = Category.objects.all()
    if catg_id:
        cate = Category.objects.get(id=catg_id)
        qs=product.objects.filter(category=cate)
        response = render(request,"shop/index.html",context={"qs":qs,'cate':categories,'cname':cname})
    else:
        qs = product.objects.all()
        response = render(request,"shop/index.html",context={"qs":qs,'cate':categories,'cname':cname})
    return response
def Signup(request):
    if request.method=='GET':
        response=render(request,"shop/Signup.html")
        return response
    
    elif request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        Email = request.POST['Email']
        phno = request.POST['phno']
        pwd = request.POST['pwd']
        repwd = request.POST['repwd']
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        error_msg = None
        if not fname or not lname or not fname.isalpha() or not lname.isalpha():
            error_msg = "First name and Last name must be alphabets and should not be empty"
        elif not uname or ' ' in uname:
            error_msg = "User name should not have spaces and should not be empty"
        elif len(pwd) < 8:
            error_msg = "Password should be greater than 8 characters"
        elif pwd != repwd:
            error_msg = "Password and re-password do not match"
        elif not Email or not re.fullmatch(regex, Email):
            error_msg = "Enter a valid email"
        elif not phno.isdigit() or len(phno) != 10:
            error_msg = "Enter a valid mobile number"
        if error_msg: 
            response = render(request, "shop/Signup.html",{'msg':error_msg})
            return response
        try:
            c=Customer.objects.create(User_name=uname,First_name=fname,last_name=lname,email=Email,mobile=phno,password=pwd)
            c.save()
            return redirect(home) 
           
        except:
            error_msg="User name or Email already exits pls try another names"
            response=render(request,"shop/Login.html",{'msg':error_msg})
            return response
def SignIn(request):
    if request.method=='GET':
        response=render(request,"shop/Login.html")
        return response
    elif request.method=="POST":
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        try:
            user = Customer.objects.get(Q(User_name=uname)&Q(password=pwd))
            request.session['cname']=uname
            return redirect("home")
        except:
            error_msg="user name and password did not match forget password"
            response = render(request, "shop/Login.html",{'msg':error_msg})
            return response
def addToCart(request, product_id):
        qs = product.objects.all()
        categories = Category.objects.all()
        cart_product = product.objects.get(id=product_id)
        cname = request.session.get('cname',None)
        
        
        if not cname:
            return redirect('login')
        try:
            customer=Customer.objects.get(User_name=cname)
        except Customer.DoesNotExist:
            return redirect('login')
        
        cart_item, created = Cart.objects.get_or_create(customer=customer, product=cart_product)

        if not created:
            cart_item.quantity += 1
            cart_item.save()
            return redirect('category')
        else:
            return redirect('category')
def view_cart(request):
    cname = request.session.get('cname', "")
    if not cname:
        return redirect('login')
    customer = Customer.objects.get(User_name=cname)

    cart_items = Cart.objects.filter(customer=customer)
    
    # Calculate the total price of the cart
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'cname':cname
    }
    
    return render(request, 'shop/cart.html', context)
def update_quantity(request,item_id):
    action = request.POST.get('action')
    item = Cart.objects.get(id=item_id)
    if action=='increase':
        item.quantity+=1
    elif action=='decrease' and item.quantity >1:
        item.quantity-=1
    item.save()
    return redirect('viewcart')
def remove_item(request,item_id):
    item = Cart.objects.get(id=item_id)
    item.delete()
    return redirect('viewcart')
def place_order(request):
    return HttpResponse("<h2>Thank You for Order</h2>")
    


def logout(request):
    if 'cname' in request.session:
        del request.session['cname']
        return redirect('login')
    else:
        return redirect("SignIn")



        
        


            



