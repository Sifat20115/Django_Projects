#from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"index.html",{'student' : [{'name':'sifat','id':'10'},{'name':'sif','id':'20'}]})