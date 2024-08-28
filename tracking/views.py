import json
from django.http import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .utils import csv_handler

# Create your views here.


def home(request: HttpRequest) -> HttpResponse | JsonResponse:
    if request.method == "POST":
        order = {
            "id": request.POST.get("id"),
            "name": request.POST.get("name"),
            "username": request.POST.get("username"),
            "status": request.POST.get("status"),
        }
        csv_handler.append_csv("./data/orders.csv", order)
    orders = csv_handler.read_csv("./data/orders.csv")
    return render(request, "tracking/index.html", {"orders": orders})
