from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request,"./first_app_idx/index.html",{'arr' : [1,2,3,4]})