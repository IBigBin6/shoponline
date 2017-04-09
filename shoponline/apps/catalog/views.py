#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.contrib import auth
# Create your views here.
from .models import Category,Product,Cart
from django.contrib.auth.models import User

def register(request,template_name):
    if request.POST:
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        email=request.POST.get('email','')
        alert=""
        try:
            u= User.objects.get(username=username)
        except:
            user=User.objects.create_user(username=username,password=password,email=email)
            user.save()
            alert="注册成功！"
            return render(request,template_name,locals())
            pass

        alert="用户名已经使用，可以直接登录！"
        return render(request,template_name,locals())
    return render(request,template_name)

def index(request,template_name):
    page_title='Welcome to the shop'
    p=Product.objects.all()
    cart=request.session.get('cart',[])
    request.session['cart']=cart
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    logout=request.POST.get('logout')
    user=auth.authenticate(username=username,password=password)

    if user is not None and user.is_active:
        auth.login(request,user)

    if logout=='Y':
        auth.logout(request)

    if request.POST.get('del_index'):
        rowIndex=request.POST.get('del_index')
        request.session['cart'].pop(int(rowIndex))

    return render(request,template_name,locals())

def show_product(request,template_name,product_name):
    p=Product.objects.get(name=product_name)
    page_title=p.name
    cart=request.session.get('cart',[])
    request.session['cart']=cart

    if request.POST.get('add_name'):
        newp=Product.objects.get(name=request.POST['add_name'])
        request.session['cart'].append(newp)

    if request.POST.get('del_index'):
        rowIndex=request.POST.get('del_index')
        request.session['cart'].pop(int(rowIndex))

    return render(request,template_name,locals())



