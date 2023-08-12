#from django.http import HttpResponse  
from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request,"./first_app_idx/index.html",{'arr' : 'sifat','Jolil' : 'Kamla'})