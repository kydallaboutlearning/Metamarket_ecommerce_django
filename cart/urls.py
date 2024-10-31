from django.urls import path
from .views import (cart_detail, 
                   cart_add,
                   cart_remove
                   )

app_name = 'cart'

#adding the paths
urlpatterns = [
    path('', cart_detail, name = 'cart_detail' ),
    path('add_to_cart/<int:product_id>/', cart_add, name ='add_to_cart'),
    path('remove/<int:product_id>/', cart_remove, name = 'remove_cart')
]