import json
from django.http import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from .utils import csv_handler

# Create your views here.


def home(request: HttpRequest) -> HttpResponse | JsonResponse:
    if request.method == "POST":
        payload = json.loads(request.body)
        csv_handler.append_csv("./tracking/orders.csv", payload)
        return HttpResponse("OK")
    elif request.method == "GET":
        return JsonResponse({"orders": csv_handler.read_csv("./tracking/orders.csv")})
