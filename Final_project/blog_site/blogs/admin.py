from django.contrib import admin
from .models import blogs,favorites,ratings

# Register your models here.

admin.site.register(blogs)
admin.site.register(favorites)
admin.site.register(ratings)