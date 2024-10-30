#importing requirements
from django.urls import path
from .views import CreateOrderView

app_name = 'orders'

url_patterns = [
    path('order_create/',CreateOrderView(), name = 'create_order')
]