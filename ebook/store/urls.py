from django.urls import path


from . import views
urlpatterns=[
   path('',views.store_view),
   path('new/',views.store_new_view.as_view()),
   path('cart/',views.cart_view),
   
]