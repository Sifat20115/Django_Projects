from django.urls import path
from . import views
urlpatterns = [
    #path('',views.TemplateView.as_view(template_name = "home.html")),#Render without view
    path('<int:roll>/', views.MyTemplateView.as_view(), {'author':'rahim'},name='homepage'),
    #path('EntryBooks/',views.store_book,name='EntryBooks'),
    path('EntryBooks/',views.BookFormView.as_view(),name='EntryBooks'),
    #path('bookstore/',views.show_book,name='bookstore'),
    path('show_books/', views.BookListView.as_view(), name='bookstore'),#all books
    path('show_books_details/<int:pk>', views.BookDetailsView.as_view(), name='bookdetails'),#all books details
    #path('editbook/<int:id>',views.edit_book,name='edit'),
    path('editbook/<int:pk>',views.BookUpdateView.as_view(),name='edit'),#PK use korte hoy update er jonno
    #path('deletebook/<int:pk>',views.delete,name='delete'),
    path('deletebook/<int:pk>',views.DeleteBookView.as_view(),name='delete'),
]
