from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def login_view(request):
    return render(request, "login.html")


def register_view(request):
    return render(request, "register.html")

def dashboard_view(request):
    return render(request, "dashboard.html")