from django.shortcuts import render
from blogs.models import blogs
# Create your views here.
def home(request):
    allblogs = blogs.objects.all().order_by('-avg')
    return render(request, 'index.html',{'blogs':allblogs})