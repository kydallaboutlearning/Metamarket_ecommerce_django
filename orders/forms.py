"""Importing required Items"""
from django import forms
from .models import Order, OrderItem

""""Creating a model form from Oder models"""

class OrderCreateform(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'first_name',
            'last-name',
            'email',
            'postal_code',
            'address',
            'created',
            'city'
            ]
        
        
        
    