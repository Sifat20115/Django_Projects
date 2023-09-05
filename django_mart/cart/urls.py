from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.cart, name='cart'),
    path('<int:product_id>/', views.add_to_cart, name='addcart'),
    path('<int:product_id>/', views.baraise, name='jog'),
    path('remove_cart_item/<int:product_id>/', views.komaise, name='biyog'),
    path('remove_cart/<int:product_id>/', views.remove, name='baad'),
    
]
