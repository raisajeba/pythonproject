from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create_product/',views.create_product,name= 'create_product'),
    path('update_product<int:id>/',views.update_product,name='update_product'),
    path('update_delete<int:id>/',views.delete_product,name = 'delete_product'),
]