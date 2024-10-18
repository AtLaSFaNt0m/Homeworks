
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'), 
    path('cart/', views.cart, name='cart'), 
    path('add-to-cart/<int:game_id>/', views.add_to_cart, name='add_to_cart'),
]
