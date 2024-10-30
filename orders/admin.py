from django.contrib import admin


#importing models
from .models import *


#creating a modelinline admin

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['order',
                     'product',
                     ]
    


#creating a decorator to register the models
@admin.register(Order)

#creating an admin class for orders
class OrderAdmin(admin.ModelAdmin):
    """Creating a list display to show fields that would display in the admin panel"""
    list_display = [
        'id',
        'first_name',
        'last_name',
        'email',
        'address',
        'postal_code',
        'created',
        'updated',
        'city',
        'paid',
        ]
    list_filter = [
        'paid',
        'created',
        'updated',
    ]
    inlines = [OrderItemInline]