from django.shortcuts import render
from .models import Product

# Create your views here.
def product(request):
    return render(request,'products/product.html' )

def products(request):
    pro = Product.objects.all()
    #x = {'pro':pro.filter(price__range=[12,101])}
    x = {'pro':Product.objects.all()}
    return render(request, 'products/products.html',x)
