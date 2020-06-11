from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import *

# Create your views here.
def dahsboard(request):
    if request.method == 'GET':
        product_obj = Product.objects.filter(is_deleted = False)
        print("Products",product_obj)
        return render(request, "tea_shop/dashboard.html",{"products":product_obj})

def add_product(request):
    if request.method == 'GET':
        return render(request, "tea_shop/add_product.html")
    
    if request.method == 'POST':
        prod_name = request.POST['prod_name'].strip()
        prod_description = request.POST["prod_description"].strip()
        prod_price = request.POST["prod_price"].strip()
        # prod_img = request.POST['prod_img']
        prod_img = request.FILES.get('prod_img')
        print("\n")
        print(prod_name)
        print(prod_description)
        print(prod_price)
        print(request.FILES.get('prod_img'))
        print(request.POST)
        print("\n")
        try:
            product_obj = Product.objects.get(prod_name = prod_name,is_deleted = False)
            msg = "Product Already Exists...!"
            url = "/add-product/"
            return render(request, "tea_shop/add_product.html",{"msg":msg,"url":url})
        except ObjectDoesNotExist:
            product_obj = Product.objects.create(
                prod_name = prod_name,
                prod_desc = prod_description,
                prod_price = prod_price,
                prod_image = prod_img,
            )
            product_obj.save()
            msg = "Product Added Successfully...!"
            url = "/"
            return render(request, "tea_shop/add_product.html",{"msg":msg,"url":url})

def view_product(request, prod_id):
    if request.method == 'GET':
        try:
            product_obj = Product.objects.get(id=prod_id, is_deleted=False)
            return render(request, "tea_shop/view_product.html",{"product":product_obj})
        except ObjectDoesNotExist:
            msg = "Product Not found...!"
            url = "/"
            return render(request, "tea_shop/dashboard.html",{"msg":msg,"url":url})

def remove_product(request, prod_id):
    if request.method == 'GET':
        try:
            product_obj = Product.objects.get(id=prod_id, is_deleted=False)
            product_obj.is_deleted = True
            product_obj.save()
            msg = "Product Removed Sucessfully...!"
            url = "/"
            return render(request, "tea_shop/dashboard.html",{"msg":msg,"url":url})
        except ObjectDoesNotExist:
            msg = "Product Not found...!"
            url = "/"
            return render(request, "tea_shop/dashboard.html",{"msg":msg,"url":url})