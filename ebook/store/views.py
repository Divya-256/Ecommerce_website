# from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def store_view(request):
    return HttpResponse("<h1>this is the store!!!!!!</h1>")

def product(request):
    return HttpResponse("<h1>this is the first product</h1>")