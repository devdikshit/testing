from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Products
from math import ceil
from django.contrib import messages
from django.contrib.auth.models import User , auth
from .forms import ProductForm
from django.views.generic import CreateView

from django.contrib.auth.decorators import login_required

# Create your views here.
# class PersonCreateView(CreateView):
#     model = Products
#     fields = '__all__'

def index(request):
    products=Products.objects.all()
    n=len(products)
    nSlides=n//4 + ceil((n/4)-(n//4))

    params={'products':products,'no_of_slides':nSlides, 'range':range(1,nSlides)}
    return render(request,'shop/index.html', params)

def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['user_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
        user.save()
        print("Success")   
        messages.info(request,"Registration")
        return redirect('/thnku')

    else:
        return render(request,'shop/register.html')

def login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        password=request.POST['pw']

        user=auth.authenticate(username=uname,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,"Login")
            return redirect('/thnku')
        else:
            messages.info(request,'Invalid User')
            return redirect('/login')
    else:
        return render(request,'shop/login.html')


def logout(request):
    auth.logout(request)
    messages.info(request,"logout")
    return redirect('/shop/thnku')

def thnku(request):
    return render(request,'shop/thnku.html')


def search(request):
    return render(request,'shop/from.html')

@login_required(login_url='/login/')
def additem(request,id=0):
    if request.method=='POST':
        if id==0:
            form=ProductForm(request.POST, request.FILES)
            print("update54153")

        else:
            product=Products.objects.get(id=id)
            form=ProductForm(request.POST, request.FILES, instance=product)
            print("updated")
        if form.is_valid():
            form.save()
            return redirect('/shop')
        else:
            return redirect('/shop/additem')

    else:
        if id==0:
            form=ProductForm()
        else:
            product=Products.objects.get(id=id)
            form=ProductForm(instance=product)
    return render(request,'shop/contact.html',{'form':form})

def delete_view(request, id):
    product=Products.objects.get(id=id)
    # form=ProductForm(instance=product)
    product.delete()
    return redirect('/shop')
    # return render(request,'shop/contact.html',)

def productview(request):
    product=Products.objects.all()
    data=product
    return render(request,'shop/productview.html',{'product':product})


def checkout(request):
    return render(request,'shop/checkout.html')
