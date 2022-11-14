from django.contrib import admin

# Register your models here.
from .models import Ebook, Cart_Items

@admin.register(Ebook)
class EbookAdmin(admin.ModelAdmin):
    list_display = ['title','price','cover_urls']


@admin.register(Cart_Items)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['title','price']