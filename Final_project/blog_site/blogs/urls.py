from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('create/',views.create,name='create'),
    path('details/<int:blog_id>',views.details,name='details'),
    path('edit/<int:blog_id>',views.edit,name='edit'),
    path('delete/<int:blog_id>',views.delete,name='delete'),
    path('favorites/<int:blog_id>',views.fav,name='fav'),
    path('removefav/<int:blog_id>',views.removefav,name='removefav'),
    path('myFav/',views.myFav,name='myFav'),
    path('filters/',views.filters,name='filters'),
    path('specific/<int:catid>',views.specific,name='specific'),
    path('rating/<int:num>/<int:blog_id>',views.rating,name='rating'),
]