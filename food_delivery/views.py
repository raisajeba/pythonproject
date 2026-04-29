from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'food_delivery/home.html')
def menu(request):
    return render(request,'food_delivery/menu.html')
def cart(request):
    return render(request,'food_delivery/cart.html')