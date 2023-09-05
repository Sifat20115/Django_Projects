from django.shortcuts import render,redirect
from cart.models import Cart,CartItem

def order_complete(request):
    return render(request,'orders/order_complete.html')

def place_order(request):
    total = 0
    gt = 0
    items = CartItem.objects.filter(user = request.user)
    if items.count() < 1:
        return redirect('store')
    for i in items:
        total = total + i.sub_total()
    gt = total + 5
    return render(request, 'cart/checkout.html', {'cart_items':items,'total':total,'gt':gt})

