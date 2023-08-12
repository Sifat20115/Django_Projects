from django.shortcuts import render
from . forms import *
# Create your views here.
def djangoform(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./first_app/upload/' + file.name,'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(request,"./first_app_idx/djangoForm.html",{'form':form})
    else:
        form = contactForm()
    return render(request,"./first_app_idx/djangoForm.html",{'form':form})

def StudentForm(request):
    if request.method == 'POST':
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentData()
    return render(request, './first_app_idx/djangoForm.html', {'form':form})  

def about(request):
    return render(request,"./first_app_idx/about.html")

def submit(request):
    print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('pass')
        select  = request.POST.get('select')
        return render(request,"./first_app_idx/form.html",{'name':name,'password':password,'select':select})
    else:
        return render(request,"./first_app_idx/form.html")