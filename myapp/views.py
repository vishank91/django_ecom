from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.db.models import Q
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
def index(request):
    return render(request,'index.html')

@login_required(login_url='/myapp/login_user/')
def cart(request):
    all=Cart.objects.filter(user=request.user)
    total=[]
    for i in all:
        total.append(i.total_price)
    return render(request,'cart.html',{
        "all":all,
        "total":sum(total)
    })
def checkout(request):
    if(request.method=='POST'):
        form=Checkout_form(request.POST)
        if(form.is_valid()):
            form.save()
            messages.success(request,"User Details Inserted Sucessfully")
            return HttpResponseRedirect('/myapp/checkout/')
        else:
            messages.error(request,"Invalid form")
    else:
        form=Checkout_form()
    return render(request,'checkout.html',{"form":form})

def home(request):
    data=Product.objects.all()
    context = {
        'Data':data
    }
    return render(request,'sample.html',context)


def login(request):
    if request.method == 'POST':
        user_name = request.POST['user']
        passw = request.POST['password']

        try:
            user = auth.authenticate(username=user_name, password=passw)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/myapp/add_product/')
            else:
                messages.error(request, "invalid")
        except:
            messages.error(request, 'Invalid User')

    return render(request, 'login.html')

def login_user(request):
    if request.method == 'POST':
        user_name = request.POST['user']
        passw = request.POST['password']

        try:
            user = auth.authenticate(username=user_name, password=passw)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/myapp/cart/')
            else:
                messages.error(request, "invalid")
        except:
            messages.error(request, 'welcome')

    return render(request, 'login_user.html')

def logout_user(request):
    logout(request)
    return render(request, 'option.html')


def admin_login(request):
    return render(request,'form.html',{})

def search(request):
    if request.method=='POST':
        s=request.POST['sr']
        if(s):
            match=Product.objects.filter(Q(title__icontains=s)|
                                         Q(description__icontains=s))
            if match:
                return render(request,'search.html',{"sr":match})
            else:
                messages.error(request,"No Result Found")

        else:
            return HttpResponseRedirect('/myapp/search/')
    return render(request,'search.html')

@login_required(login_url='/myapp/login_admin/')
def add_product(request):
    if request.method=='POST':
        form=Product_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Product Add Successfully")
            return HttpResponseRedirect('/myapp/add_product/')
        else:
            messages.error(request,"Invalid form")
    else:
        form=Product_form()

    return render(request,'form.html',{"form":form})
@login_required(login_url='/myapp/login/')
def product(request,id):
    product=Product.objects.get(id=id)
    if(request.method=='POST'):
        form=Cart_form(request.POST)
        q=request.POST['quantity']
        if(form.is_valid()):
            f=form.save(commit=False)
            f.user=request.user
            f.product=product
            f.quantity=q
            f.total_price=float(product.price)*float(q)
            f.save()
            return HttpResponseRedirect('/myapp/cart/')
    else:
        form=Cart_form()
    return render(request,'product-details.html',{
        "detail":product,
        "form":form
    })

def delete_cart_item(request,item_id):
    match=Cart.objects.get(id=item_id)
    match.delete()
    return HttpResponseRedirect('/myapp/cart/')


def register(request):
    if request.method=='POST':
        form=User_form(request.POST)
        if form.is_valid():
            name=form.cleaned_data['username']
            emailid=form.cleaned_data['email']
            first=form.cleaned_data['first_name']
            last=form.cleaned_data['last_name']
            passw=form.cleaned_data['password']

            User.objects.create_user(username=name,email=emailid,first_name=first,last_name=last,password=passw)

            messages.success(request,"User Registration Successfully")
            return HttpResponseRedirect('/myapp/login_user/')
    else:
        form=User_form()
    return render(request,'registration.html',{"form":form})

def login_option(request):
    return render(request,'option.html')

def shop(requset):
    cat=Categories.objects.all()
    default='Mobile'
    all_items=Product.objects.filter(category__name=default)
    return render(requset,'shop.html',{
        "cat":cat,
        "all_items":all_items,
    })

def shop2(requset,cat_name):
    cat=Categories.objects.all()
    default='Mobile'
    all_items=Product.objects.filter(category__name=cat_name)
    return render(requset,'shop.html',{
        "cat":cat,
        "all_items":all_items,
    })