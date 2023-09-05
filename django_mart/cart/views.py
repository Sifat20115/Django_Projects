from django.shortcuts import render,redirect
from store.models import Product
from cart.models import Cart,CartItem
# Create your views here.
def get_create_session(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def cart(request):
    cart_items = None
    total = 0
    gt = 0
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user = request.user)
        for i in cart_items:
            total = total + i.sub_total()
        gt = total + 5
    else:
        session_id = get_create_session(request)
        cart_id = Cart.objects.get(cart_id = session_id)
        is_exist = Cart.objects.filter(cart_id = session_id).exists()
        
        if is_exist:
            cart_items = CartItem.objects.filter(cart = cart_id)
            for i in cart_items:
                total = total + i.sub_total()
            gt = total + 5
        print(cart_items)
    return render(request,'cart/cart.html',{'cart_items':cart_items,'total':total,'gt':gt})

def add_to_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    session_id = get_create_session(request)
    if request.user.is_authenticated:
        cart_item = CartItem.objects.filter(product = product, user = request.user).exists()
        if cart_item:
            item = CartItem.objects.get(product = product)
            item.quantity += 1
            item.save()
        else:
            cart_id = Cart.objects.filter(cart_id = session_id).exists()
            if cart_id:
                cart_id = Cart.objects.get(cart_id = session_id)
                item = CartItem.objects.create(
                product = product,
                cart = cart_id,
                user = request.user,
                quantity = 1,
                )
                item.save()
            else:
                cart = Cart.objects.create(cart_id = session_id)
                cart.save()
                cart_id = Cart.objects.get(cart_id = session_id)
                item = CartItem.objects.create(
                product = product,
                cart = cart_id,
                user = request.user,
                quantity = 1,
                )
    else:
        cart_id = Cart.objects.filter(cart_id = session_id).exists()
        
        if cart_id:
            cart_item = CartItem.objects.filter(product = product).exists()
            if cart_item:
                item = CartItem.objects.get(product = product)
                item.quantity += 1
                item.save()
            else:
                cart_id = Cart.objects.get(cart_id = session_id)
                item = CartItem.objects.create(
                product = product,
                cart = cart_id,
                quantity = 1,
                )
                item.save()
        else:
            cart = Cart.objects.create(cart_id = session_id)
            cart.save()
            cart_id = Cart.objects.get(cart_id = session_id)
            item = CartItem.objects.create(
                product = product,
                cart = cart_id,
                quantity = 1,
            )
            item.save()
    return redirect('cart')

def baraise(request,product_id):
    product = Product.objects.get(id=product_id)
    item = CartItem.objects.get(product = product)
    item.quantity += 1
    item.save()
    return redirect('cart')
def komaise(request,product_id):
    product = Product.objects.get(id=product_id)
    item = CartItem.objects.get(product = product)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('cart')
def remove(request,product_id):
    product = Product.objects.get(id=product_id)
    item = CartItem.objects.get(product = product)
    item.delete()
    return redirect('cart')

