from django.urls import path


from . import views
urlpatterns=[
   path('',views.store_view),
   path('p1',views.product)
]