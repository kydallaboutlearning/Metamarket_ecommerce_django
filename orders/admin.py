from django.contrib import admin


#importing models
from .models import *


#creating a modelinline admin

class order(admin.TabularInline):
    model = OrderItems
    raw_id_fields = ['price','product','quantity']