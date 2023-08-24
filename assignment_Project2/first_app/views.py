from django.shortcuts import render,redirect
from first_app.forms import taskForm
from first_app.models import taskFormModel
# Create your views here.

def home(request):
    return render(request,'home.html')

def create(request):
    if request.method == 'POST':
        task = taskForm(request.POST)
        if task.is_valid():
            print(task.cleaned_data)
            task.save()
            return redirect('show')
    else:
        task = taskForm()
    return render(request,'taskForm.html',{'task':task})

def show(request):
    see = taskFormModel.objects.all()
    print(see)
    return render(request,"show_tasks.html",{'task' : see})

def edit(request,id):
    task = taskFormModel.objects.get(pk = id)
    form = taskForm(instance = task)
    if request.method == 'POST':
        form = taskForm(request.POST,instance = task)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('show')
    return render(request,"taskForm.html",{'task': form})

def delete(request,id):#DELETE
    task = taskFormModel.objects.get(pk = id).delete()
    return redirect('show')

def complete(request,id):
    task = taskFormModel.objects.get(pk = id)
    task.status = True
    task.save()
    see = taskFormModel.objects.all()
    return render(request,"com_tasks.html",{'task' : see})

def completepage(request):
    see = taskFormModel.objects.all()
    return render(request,"com_tasks.html",{'task' : see})