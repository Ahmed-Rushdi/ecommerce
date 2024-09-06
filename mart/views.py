from django.http import HttpRequest
from django.shortcuts import render, HttpResponse
from .models import Product


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    items = Product.objects.filter(is_available=True)
    print(list(items))
    return render(request, "mart/index.html", {"items": items})


def cart(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        product_ids = [request.GET[i] for i in request.GET]
        selected_products = Product.objects.filter(id__in=product_ids)
    return render(request, "mart/cart.html", {"items": selected_products})
