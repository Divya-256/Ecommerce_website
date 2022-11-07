from django.shortcuts import render
from .models import Ebook
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def store_view(request):
    ebooks={'ebooks':Ebook.objects.all()}
    return render(request,'store\index.html',ebooks)

def cart_view(request):
    return render(request,'store\cart.html')


@csrf_exempt
def add_item(request):
    book_id=request.POST['book_id']
    title=Ebook.objects.get(pk=book_id).title
    price=Ebook.objects.get(pk=book_id).price
    
