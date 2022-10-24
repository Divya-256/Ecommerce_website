from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("""
    <h1>Welcome to ebook store</h1>
    <img src="https://images.pexels.com/photos/159866/books-book-pages-read-literature-159866.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" >
    
    
    """)