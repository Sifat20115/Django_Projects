from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth import login,logout,authenticate
from cart.models import Cart,CartItem
# Create your views here.
def get_create_session(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = form.save()
            login(request,user)
            return redirect('cart')
        
    return render(request,'accounts/register.html',{'form':form})



def profile(request):
    return render(request,'accounts/dashboard.html')
def user_login(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(username = un,password = passw)
        session_id = get_create_session(request)
        cart = Cart.objects.get(cart_id = session_id)
        is_cart_item_exists = CartItem.objects.filter(cart = cart).exists()
        if is_cart_item_exists:
            cart_item = CartItem.objects.filter(cart = cart)
            for i in cart_item: 
                i.user = user
                i.save()
        login(request,user)
        return redirect('profile')
    return render(request,'accounts/login.html')

def user_logout(request):
    logout(request)
    return render(request,'accounts/login.html')