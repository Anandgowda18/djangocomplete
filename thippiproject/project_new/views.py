from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'project_new/index.html')

def electronics(request):
    products = {
        'goods_available':'Electronics available',
        'product1':'Apple',
        'product2':'Mobiles',
        'product3':'Laptops'}
    return render(request,'project_new/products.html',products)

def toys(request):
    products = {
        'goods_available':'Toys available',
        'product1':'remote car',
        'product2':'helicopter',
        'product3':'train'}
    return render(request,'project_new/products.html',products)

def shoes(request):
    products = {
        'goods_available':'Shoes available',
        'product1':'Adidas',
        'product2':'Nike',
        'product3':'UnderArmour'}
    return render(request,'project_new/products.html',products)
