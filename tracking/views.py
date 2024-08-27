import json
from django.shortcuts import HttpResponse
from .utils import csv_handler

# Create your views here.


def home(request):
    if request.method == "POST":
        payload = json.loads(request.body.decode("utf-8"))
        csv_handler.append_csv("./tracking/orders.csv", payload)
        return HttpResponse("OK")
    elif request.method == "GET":
        return HttpResponse(csv_handler.read_csv("./tracking/orders.csv"))
