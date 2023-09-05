from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('signin/',views.signin,name='signin'),
    path('login/',views.user_login,name='login'),
    path('profile/', views.profile, name='profile'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('logout/',views.user_logout,name='logout'),
]
