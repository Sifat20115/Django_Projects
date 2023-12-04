from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('stuCreate/',views.studentApi.as_view(),name='stuCreate'),
    path('stuget/',views.studentApi.as_view(),name='stuget'),
    path('stuupdate/',views.studentApi.as_view(),name='stuupdate'),
    path('studelete/',views.studentApi.as_view(),name='studelete')
]
