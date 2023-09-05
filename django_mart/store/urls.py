from django.shortcuts import render, get_object_or_404, redirect
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('product_detail/', views.product_detail, name='prodetail'),
]