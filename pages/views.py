from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def service(request):
    return render(request, "services.html")

def terms_of_service(request):
    return render(request, "terms-of-service.html")

def google_verification(request):
    return render(request, "google4872331c416f8761.html")
