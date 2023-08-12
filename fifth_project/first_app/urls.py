from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('about/',views.about,name='about'),
    path('form/',views.submit,name='submit'),
    path('djangoform/',views.djangoform,name='djf'),
    path('stuform/',views.StudentForm,name='stf')
]