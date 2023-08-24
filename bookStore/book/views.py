#from django.http import HttpResponse
from django.shortcuts import render,redirect
from book.form import *
from book.models import *
from django.views.generic import TemplateView
# Create your views here.
#username:sifat,pass:lol.lmao6932S
#def home(request):
    #return render(request,"home.html")

#-------------CRUD OPERATION-------------

def store_book(request):#CREATE
    if request.method == 'POST':
        books = bookStoreForm(request.POST)
        if books.is_valid():
            print(books.cleaned_data)
            books.save()
            return redirect('bookstore')
    else:
        books = bookStoreForm()
    return render(request,"books.html",{'form': books})

def show_book(request):#READ
    book = BookStoreModel.objects.all().order_by('id')
    print(book)
    return render(request,"show_books.html",{'book' : book})

def edit_book(request,id):#UPDATE
    book = BookStoreModel.objects.get(pk = id)
    form = bookStoreForm(instance = book)
    if request.method == 'POST':
        form = bookStoreForm(request.POST,instance = book)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('bookstore')
    return render(request,"books.html",{'form': form})

def delete(request,id):#DELETE
    book = BookStoreModel.objects.get(pk = id).delete()
    return redirect('bookstore')