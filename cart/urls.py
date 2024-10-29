from django.urls import path
from . import views

app_name = 'cart'

#adding the paths
urlpatterns = [
    path('', views.cart_detail, name = 'cart_detail' ),
    path('add_cart/<int:product_id>/', views.cart_add, name ='add_to_cart'),
    path('remove/<int:product_id>/', views.cart_remove, name = 'remove_cart')
]