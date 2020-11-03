from django.shortcuts import render, redirect
from products.forms import ProductForm
# from products.models import Product
from .models import *

'''
def product_create(request):
    return render(request, 'product_create.html')
'''


def home(request):
    products = Product.objects.all()
    print(products)
    context = {'products':products}
    return render(request, 'home.html', context)

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')

    else:
        form = ProductForm()
        return render(request,'product_create.html',{'form':form})

def success(request): 
    return HttpResponse('successfully uploaded') 

def product_display(request):
    obj = Product.objects.all()
    
    return render(request, 'product_display.html', {'obj':obj})

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')


