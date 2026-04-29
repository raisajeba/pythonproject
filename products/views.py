from django.shortcuts import render, redirect
from products.forms import ProductForm
# Create your views here.
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('/')
    else:
        form = ProductForm()
        return render(request,'forms.html',{'form':form})

from .models import Product
def update_product(request,id):
    p = Product.objects.get(pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=p)
        if form.is_valid():
          form.save()
          return redirect('/')
    else:
        form = ProductForm(instance=p)
        return render(request,'forms.html',{'form':form})
def delete_product(request,id):
    Product .objects.get(pk=id).delete()
    return redirect('/')