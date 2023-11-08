from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('stuCreate/',views.student_Create,name='stuCreate'),
    path('stuget/',views.student_get,name='stuget')
]