from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:roll>',views.delete,name='delete'),
    path('form/',views.form,name='form'),
]