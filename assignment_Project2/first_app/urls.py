from django.urls import path
from first_app.views import *
urlpatterns = [
    path('',home,name='home'),
    path('create_task/',create,name='create'),
    path('show_tasks/',show,name='show'),
    path('delete_tasks/<int:id>',delete,name='delete'),
    path('edit_tasks/<int:id>',edit,name='edit'),
    path('complete_tasks/<int:id>',complete,name='complete'),
    path('complete_tasks/',completepage,name='completepage'),
]
