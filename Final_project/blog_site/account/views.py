from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import login,logout,authenticate
from blogs.models import blogs
# Create your views here.
def signin(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print('Valid')
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request,"account/register.html",{'form':form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username = name, password = userpass) # check kortechi user database e ache kina
            if user is not None:
                login(request, user)
                return redirect('home') # profile page e redirect korbe    
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form':form})

def profile(request):
    allblogs = blogs.objects.filter(user = request.user).order_by('-avg')
    return render(request,'account/profile.html',{'blogs':allblogs})
    
def user_logout(request):
    logout(request)
    return redirect('home')

def about(request):
    return render(request,'account/about.html')

def contact(request):
    return render(request,'account/contact.html')