from django.shortcuts import render
from cart.cart import Cart
from .models import OrderItem, Order

from .forms import OrderCreateform
# Create your views here.

def CreateOrderView(request):

    #getting the Existing cart
    cart = Cart(request)
    form = OrderCreateform()

    
    
    #creating a method to handle post request
    if request.method == 'POST':

            #getting if order info is saved before
        create_order_form = OrderCreateform(request.POST)

        if create_order_form.is_valid():
                #saving the order
                order = create_order_form.save()
                #create an instance of the item in the cart to save in the database
                for item in cart:
                    OrderItem.objects.create(
                        order = order,
                        product = item['product'],
                        price = item['price'],
                        quantity = item['quantity']
                        )
                
                #deleting the cart
                cart.clear()
                return render(request, 
                          'orders/success.html',
                          {'order':order}
                          )
        else:
            form = OrderCreateform()
    else:
            form = OrderCreateform()

    return render(
        request,
        'orders/create_order.html', 
        {'form':form,'cart':cart},
    )



