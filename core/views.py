from django.shortcuts import render

# Create your views here.


def home_core(request):
    return render(request, "home_core.html")


def product_project(request):
    return render(request, "product.html")
