from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'books', views.BookViewSet,basename="books")

urlpatterns = [
    #path('books/',views.bookListView.as_view()),#Get ar Post request handle korbe 
    #path('books/<int:pk>/',views.BookListUpdateDelete.as_view()),#Update ar delete request handle korbe
    
    #path('books/',views.BookListCreateAPIView.as_view()),#Get ar Post request handle korbe 
    #path('books/<int:pk>/',views.BookRetrieveUpdateDestroyAPIView.as_view()),#Update ar delete request handle korbe
    
    path('',include(router.urls)),
]