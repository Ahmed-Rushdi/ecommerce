from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpRequest, HttpResponse

# Create your views here.


def handle_register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("/")
    else:
        form = UserCreationForm()

    return render(request, "users/register.html", {"form": form})


def handle_login(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            return redirect("/")
        else:
            print(form.errors)
    else:
        form = AuthenticationForm()
        # form.fields["username"].widget.attrs["class"] = "w-full"
        # form.fields["password"].widget.attrs["class"] = "w-full"
        # form.fields["username"].widget.attrs["placeholder"] = "Username"
        # form.fields["password"].widget.attrs["placeholder"] = "Password"
    return render(request, "users/login.html", {"form": form})


def handle_logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("/")
