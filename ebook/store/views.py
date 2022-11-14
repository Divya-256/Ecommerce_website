from django.shortcuts import render,HttpResponseRedirect
from .models import Ebook,Cart_Items
from django.views.generic import ListView
# Create your views here.

def store_view(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        book = Ebook.objects.filter(id=book_id).first()
        cart = Cart_Items.objects.create(title=book.title,price=book.price)
        cart.save()

    ebooks={'ebooks':Ebook.objects.all()}
    return render(request,'store\index.html',ebooks)

class store_new_view(ListView):
    model = Ebook
    template_name = 'store\index.html'
    context_object_name ='ebooks'

def cart_view(request):
    CART_ITEMS=Cart_Items.objects.all()
    cart_total =0
    for items in CART_ITEMS:
        cart_total+=items.price
    
    return render(request,'store\cart.html',{
        'cart_items':CART_ITEMS,
        'cart_total':cart_total
    })

def del_cart_items(request):
        CART_ITEMS=Cart_Items.objects.all()
        if request.method== "POST":
            item_id = request.POST['item_id']
            Cart_Items.objects.get(pk=item_id).delete()
        return HttpResponseRedirect('/store/cart')
        
     
    
        
    


