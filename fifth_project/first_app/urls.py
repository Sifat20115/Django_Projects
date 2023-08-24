from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('about/',views.about,name='about'),
    path('form/',views.submit,name='submit'),#Eta html diye banano form
    path('djangoform/',views.djangoform,name='djf'),#eta django te class create kore kora form
    path('stuform/',views.StudentForm,name='stf')
]