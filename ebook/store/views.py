from django.shortcuts import render
from .models import Ebook
# Create your views here.

def store_view(request):
    ebooks={'ebooks':Ebook.objects.all()}
    return render(request,'store\index.html',ebooks)

def cart_view(request):
    return render(request,'store\cart.html')
