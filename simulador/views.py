from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def index(request: HttpRequest):
    return render(request, 'simulador/index.html')