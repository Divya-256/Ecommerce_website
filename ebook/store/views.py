from django.shortcuts import render

# Create your views here.

def store_view(request):
    return render(request,'store\index.html')

