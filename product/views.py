from django.shortcuts import render
from .models import Product

# Create your views here.
def product(request):
    return render(request, 'product/product.html')

def products(request):
    pro = Product.objects.all()
    x= {'product':pro.filter(name__contains=('')).filter(price__range =[10,500])}
    return render(request, 'product/products.html', x)