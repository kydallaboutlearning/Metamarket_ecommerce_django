from django.shortcuts import render
from cart.cart import Cart
from .models import OrderItem, Order

from .forms import OrderCreateform
# Create your views here.

def CreateOrderView(request):

    #getting the Existing cart
    cart = Cart(request)

    #getting user order info
    order_info = Order.objects.filter().values_list().first()
    if order_info :
            #saving the values into the form 
            order = OrderCreateform(  request.POST , initial = {
                  'first_name':order_info[0],
                  'last_name':order_info[1],
                  'email':order_info[2],
                  'address':order_info[3],
                  'postal_code':order_info[4],
                  'city':order_info[7]
                  })
            if order.is_valid():
                order.save()
                #create an instance of the item in the cart to save in the database
                for item in cart:
                    OrderItem.objects.create(
                        order = order,
                        product = item['product'],
                        price = item['price'],
                        quantity = item['quantity']
                        )
            return render(request,'orders/create_order.html', {'form':order,'cart':cart,'order_info':order_info},
        )
    else:
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
                render(request, 
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



