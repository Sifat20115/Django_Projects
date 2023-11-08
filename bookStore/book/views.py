#from django.http import HttpResponse
from django.shortcuts import render,redirect
from book.form import *
from book.models import *
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import FormView,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
#username:sifat,pass:lol.lmao6932S
#def home(request):
    #return render(request,"home.html")

#-------------CRUD OPERATION-------------

# class based view
class MyTemplateView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        print(kwargs)
        context = {'name' : 'rahim', 'age' : 21}
        print(context)
        context.update(kwargs) #dictionary update kora
        print(context)
        return context

#Create book function based view:
'''
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
    '''
#Create book class based view:
'''
class BookFormView(FormView):#step 1
    model = BookStoreModel
    template_name = 'books.html'
    form_class = bookStoreForm
    success_url = reverse_lazy('bookstore')
    def form_valid(self, form):
        print(form.cleaned_data)
        form.save()
        return redirect('bookstore')
'''
class BookFormView(CreateView):#step 2
    model = BookStoreModel
    template_name = 'books.html'
    form_class = bookStoreForm
    success_url = reverse_lazy('bookstore')



#Function base view Show :
'''
def show_book(request):#READ
    book = BookStoreModel.objects.all().order_by('id')
    print(book)
    return render(request,"show_books.html",{'book' : book})
   '''
#class base view Show:
class BookListView(ListView):
    model = BookStoreModel
    template_name = 'show_books.html'
    context_object_name = 'booklist'
    #def get_queryset(self):
    #     return BookStoreModel.objects.filter(id='3')
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context = {'Rahim' : BookStoreModel.objects.all().order_by('author')}
    #     return context
    
    # ordering = ['-id']#shudhu eta likheo order kora jaay
    # homework
    '''
    def get_template_names(self): # template ke override korbe|Ei function category wise template show korbe
        if self.request.user.is_superuser:
            template_name = 'superuser.html'
        elif self.request.user.is_staff:
            template_name = ''
        else:
            template_name = self.template_name
        return [template_name]
'''

class BookDetailsView(DetailView):
    model = BookStoreModel
    template_name = 'book_details.html'
    context_object_name = 'item'
    pk_url_kwarg = 'pk'#primary key accept korar jonno 

#function base update view:
'''
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
'''
#class base update view:
class BookUpdateView(UpdateView):
    model = BookStoreModel
    template_name = 'books.html'
    form_class = bookStoreForm
    success_url = reverse_lazy('bookstore')



#function base delete view:
'''
def delete(request,id):#DELETE
    book = BookStoreModel.objects.get(pk = id).delete()
    return redirect('bookstore')
    '''
    
#class base delete view:
class DeleteBookView(DeleteView):
    model = BookStoreModel
    template_name = 'books.html'
    success_url = reverse_lazy('bookstore')