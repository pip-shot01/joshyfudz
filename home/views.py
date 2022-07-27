from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.generic import View


from . forms import *
from . models import *
import uuid
import json
import requests

# Create your views here.
def index(request):
    display = Product.objects.filter(display=True)
    
    context = {
        'display':display,
    }
    return render(request, 'index.html', context)

def Contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'order submitted successfully!!!')
            return redirect('index')
        else:
            messages.error(request, 'order not submitted')
            return redirect('index')
    return render(request, 'contacts.html')

@login_required(login_url='login')
def products(request):
    # morning = Catalogue.objects.filter(breakfast=True)
    # noon = Catalogue.objects.filter(lunch=True)
    # night = Catalogue.objects.filter(dinner=True)
    # snacks = Catalogue.objects.filter(pastries=True)
    # wine = Catalogue.objects.filter(drinks=True)
    product = Product.objects.filter(meals=True)
    snacks = Product.objects.filter(snacks=True)
    Wines = Product.objects.filter(wines=True)

    context = {
        'product':product,
        'snacks':snacks,
        'Wines':Wines
    }
    # context = {
    #     'morning':morning,
    #     'noon': noon,
    #     'night': night,
    #     'snacks': snacks,
    #     'wine': wine,
    # }
    return render(request, 'catalogues.html', context)

def Register(request):
    rg = RegisterForm()
    if request.method == 'POST':
        rg = RegisterForm(request.POST)
        if rg.is_valid():
            rg.save()
            messages.success(request, 'Registration Successfull!!')
            return redirect('login')
        else:
            messages.error(request, 'oops!!, Invalid Credentials')
            return redirect('register')
    return render(request, 'register.html')

def Login(request):
    if request.method == 'POST':
        usernamed = request.POST['username']
        password  =  request.POST['password']
        user = authenticate(request, username=usernamed, password=password)
        if user:
            login (request, user)
            messages.success(request, 'Login Successfull')
            return redirect('index')
        else:
            messages.error(request, 'oops!!, invalid credentials')
            return redirect('login')
    return render(request, 'login.html')

def Logout(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def details(request, id):
    detail = Product.objects.get(pk=id)
    
    context = {
        'detail':detail,
    }
    return render(request, 'details.html', context)

def profile(request):
    accounts = Profile.objects.get(user=request.user.id)
    context = {
        'accounts':accounts,
    }
    return render(request, 'profile.html', context)

@login_required(login_url='login')
def profile_update(request): 
    # profile = Profile.objects.get(user__username = request.user.username)
    update = ProfileUpdate(instance = request.user.username)      #instantiate the form for a GET request along with users details
    if request.method =='POST':
        update = ProfileUpdate(request.POST,request.FILES, instance = request.user.profile)
        if update.is_valid():
            update.save()
            messages.success(request, 'Profile update successfully')
            return redirect('index')
        else:
            messages.error(request, update.errors)
            return redirect('profile_update')
    context ={
        'profile':profile,
        'update':update,
    }    
    return render(request, 'updateprofile.html', context)


@login_required(login_url='login')
def password(request):
    # profile = Profile.objects.get(user__username = request.user.username)
    pas = PasswordChangeForm(request.user)
    if request.method == 'POST':
        pas = PasswordChangeForm(request.user, request.POST)
        if pas.is_valid():
            user = pas.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'password changed successfully')
            return redirect('index')
        else:
            messages.error(request, "passwords matching doesn't exists")
            return redirect('password')
        
    context = {
            'pas':pas,
            'profile':profile,
        }
    return render(request, 'password.html', context)


def shopcart(request):
    if request.method == 'POST':
        quant = int(request.POST['quantity'])
        item_id = request.POST['product_id']
        item = Product.objects.get(pk=item_id)
        # order_num = Profile.objects.get(user__username = request.user.username)
        # cart_no = order_num.id
        cart_no = item.id
  
        cart = Shopcart.objects.filter(user__username = request.user.username, paid = False) #Shopper with unpaid items
        if cart: #existing Shopcart with a select items
            basket = Shopcart.objects.filter(product_id = item.id, user__username = request.user.username).first()
            if basket:
                basket.quantity += quant
                basket.amount = basket.price * quant
                basket.save()
                messages.success(request, 'item added to cart')
                return redirect('products')
            else:
                newitem = Shopcart()
                newitem.user = request.user
                newitem.product = item
                newitem.quantity = quant
                newitem.price = item.price
                newitem.amount = item.price * quant
                newitem.order_no = cart_no
                newitem.paid = False
                newitem.save()
                messages.success(request, 'item added to shopcart successfully!!')
                return redirect('products')
        else:
            newcart = Shopcart()
            newcart.user = request.user
            newcart.product = item
            newcart.name_id =item.name
            newcart.amount = item.price * quant
            newcart.quantity = quant
            newcart.price = item.price 
            newcart.order_no = cart_no
            newcart.paid =False
            newcart.save()
            messages.success(request, 'item added to shopcart successfully!!')
            return redirect('products')
    else:
            newcart = Shopcart()
            newcart.user = request.user
            newcart.product = item
            newcart.quantity = quant
            newcart.name_id =item.name
            newcart.price = item.price 
            newcart.order_no = cart_no
            newcart.paid =False
            newcart.save()
            messages.success(request, 'item added to shopcart successfully!!')
            return redirect('products')
    return redirect('products')

@login_required(login_url='login')
def displaycart(request):
    trolley = Shopcart.objects.filter(user__username = request.user.username, paid = False)
    # profile = Profile.objects.get(user__username = request.user.username)
    subtotal =0
    vat = 0
    total = 0
    
    for item in trolley:
        subtotal += item.price * item.quantity
    
    vat = 0.075 * subtotal
    total = vat + subtotal
    
    context =  {
        'trolley':trolley,
        'subtotal':subtotal,
        'profile':profile,
        'vat':vat,
        'total':total,
    }
    return render(request, 'display.html', context)

@login_required(login_url='login')
def deleteitem(request):
    item_id = request.POST['item_id']
    item_delete = Shopcart.objects.get(pk = item_id)
    item_delete.delete()
    messages.success(request, 'item deleted successfully')
    return redirect('displaycart')

def increase(request):
    if request.method == 'POST':
        the_item = request.POST['itemid']
        the_quant = int(request.POST['quant'])
        modify = Shopcart.objects.get(pk=the_item)
        modify.quantity = the_quant
        modify.amount = modify.quantity * modify.price
        modify.save()
    return redirect('displaycart')

# checkout using class-based view and axios get request 
class CheckoutView(View):
    def get(self, request, *args, **kwargs):
        summary = Shopcart.objects.filter(user__username = request.user.username, paid=False)
        subtotal =0
        vat= 0
        total =0
        
        for cart in summary:
            subtotal += cart.price * cart.quantity
    
        vat = 0.075 * subtotal
        total = vat + subtotal
        
        context =  {
            'summary':summary,
            'tota':total,
        }
        
        return render(request, 'checkout.html', context)
        

def callback(request):
    # profile = Profile.objects.get(user__username = request.user.username)
    cart = Shopcart.objects.filter(user__username = request.user.username, paid= False)
    
    for pro in cart:
        pro.paid = True
        pro.save()
        
        stock = Catalogue.objects.get(pk=pro.product.id)
        stock.max_quantity-= pro.quantity 
        stock.save
        
    context = {
        'profile':profile,
    }
    return render(request, 'callback.html', context)
  
    
def pay(request):
    if request.method == 'POST':
        api_key = 'sk_test_3dc8d3616a6bbc505dc36ce12fc2f2c65dc4b5f1'
        curl = 'https://api.paystack.co/transaction/initialize'
        cburl = 'http://127.0.0.1:8000/displaycart'
        user = User.objects.get(username=request.user.username)
        email = user.email
        total = float(request.POST['total']) * 100
        cart_no = user.username
        transac_code = str(uuid.uuid4())
        
        # intergrating to paystack
        headers = {'Authorization': f'Bearer {api_key}'}
        data = {'reference': transac_code, 'amount':int(total),'email': email,'order_number':cart_no,'callback_url':cburl, 'currency':'NGN'}
        try:
            r = requests.post(curl, headers=headers, json=data)
        except Exception:
            messages.error(request, 'Network busy,refresh and try again')
        else:
            transback = json.loads(r.text)
            rdurl = transback['data']['authorization_url']
            return redirect(rdurl)
        return redirect('displaycart')