from django.urls import path


from . import views
urlpatterns=[
   path('',views.store_view),
   path('cart/',views.cart_view),
   path('cart_add_item/',views.add_item)
]