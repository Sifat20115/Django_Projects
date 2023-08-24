from django.urls import path
from . import views
urlpatterns = [
    path('',views.TemplateView.as_view(template_name = "home.html")),
    path('EntryBooks/',views.store_book,name='EntryBooks'),
    path('bookstore/',views.show_book,name='bookstore'),
    path('editbook/<int:id>',views.edit_book,name='edit'),
    path('deletebook/<int:id>',views.delete,name='delete'),
]
