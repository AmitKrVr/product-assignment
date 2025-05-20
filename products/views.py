from django.shortcuts import render, redirect, get_object_or_404    
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django import forms

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class  = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-list-view')
    else:
        form = ProductForm()
    return render(request, 'products/form.html', {'form': form})

def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})

def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/detail.html', {'product': product})