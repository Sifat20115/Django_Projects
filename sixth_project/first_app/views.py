#from django.http import HttpResponse
from django.shortcuts import render,redirect#[ekti kaaj huar pore autometic arekti page er link a nie jaabe redirect diye]
from first_app.form import *
from . import models
def home(request):
    student = models.Student.objects.all()#shob student type er object ke student table theke list kore nilam
    print(student)
    return render(request,"./first_app_idx/home.html",{'student' : student})

def delete(request,roll):
    delStu = models.Student.objects.get(pk = roll).delete()
    print(delStu)
    return redirect('home')

def form(request):
    if request.method == 'POST':
        form = stu(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = stu()
    return render(request,"./first_app_idx/form.html",{'form': form})