from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('api/',views.apiclass.as_view(),name='api'),
    #path('api2/',views.api2,name='api2'),
    path('api2/',views.apiclass2.as_view(),name='api2'),
    
    path('stuInfo/<int:num>',views.student_detail,name='stuinfo'),
    path('stuInfo/',views.student_list,name='stuList')
]
