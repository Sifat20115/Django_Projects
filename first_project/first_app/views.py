from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Ghore achi Bro...")
def dekho(request):
    return HttpResponse("Yea babe <3 <3 ")