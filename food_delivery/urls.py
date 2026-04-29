from django.urls import path
from . import views
urlpatterns =[
path('',views.home,name='food_home'),
path('menu/',views.menu,name='menu'),
path('cart/',views.cart,name ='cart'),
]