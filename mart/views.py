from django.http import HttpRequest
from django.shortcuts import render, HttpResponse

from .utils import csv_handler


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    items = csv_handler.read_csv("./data/products.csv")
    return render(request, "mart/index.html", {"items": items})


def cart(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        products = [
            request.POST.get(p) for p in request.POST if p.startswith("product-")
        ]
        selected_products = csv_handler.read_csv("./data/products.csv")
        selected_products = [p for p in selected_products if p["ProductID"] in products]
    elif request.method == "GET":
        products = [request.GET.get(p) for p in request.GET if p.startswith("product-")]
        selected_products = csv_handler.read_csv("./data/products.csv")
        selected_products = [p for p in selected_products if p["ProductID"] in products]
    return render(request, "mart/cart.html", {"items": selected_products})
