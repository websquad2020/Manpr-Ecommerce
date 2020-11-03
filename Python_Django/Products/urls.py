from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('productform/', views.product_create, name="product_create"),
    path('success', views.success, name = 'success'),
    path('product_display/', views.product_display, name = 'product_display'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('', views.home, name='home'),

] 

 
