#importing required modules
from decimal import Decimal
from django.conf import Settings
from shop.models import Product

#creating a cart class
class Cart:
    def __init__(self,request):
        """
        initializing cart session
        """
        self.session = request.session
        cart = self.session.get[Settings.CART_SESSION_ID]

        if not cart:
            cart = self.session.get[Settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self,product,quantity = 1,override_quantity = False):
        """
        adding a product or updating it's quantity
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price' : str(product.price)
            }

        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()
    #creating a save method
    def save(self):
         # mark the session as "modified" to make sure it gets saved
         self.session.modified = True

    #adding remove method 
    def remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    #creating an iteration method
    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        #getting the products from the database

        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = Decimal(item['price']) * item['quantity']
            yield item  

    #creating method to count products
    def __len__(self):
        """
        counting all items in the cart
        """
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        """
        getting total price of items
        """
        return sum(Decimal(item['price'] * item['quantity'] for item in self.cart.values))
    
    def clear(self):
        """
        method for deleting session 
        """
        del self.session.get[Settings.CART_SESSION_ID]

 



