from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Order(models.Model):
    first_name =  models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField() 
    address = models.CharField(max_length = 500)
    postal_code = models.CharField(max_length = 10)
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now_add = True)
    city = models.CharField(max_length = 100)
    paid = models.BooleanField(default = False )

    """ Adding metadata for proper placing"""
    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields = ['created']),]

    def __str__(self):
        return f'order {self.id}'
    
    def get_total_cost(self):
        sum(item.get_cost() for item in self.items.all() )
    
class OrderItems(models.Model):
    order = models.ForeignKey(Order, related_name='items' , on_delete=models.CASCADE)
    product = models.ForeignKey('shop.Product', related_name='order_items', on_delete = models.CASCADE)
    price  = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity
    




