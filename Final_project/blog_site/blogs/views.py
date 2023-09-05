from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import blogsform
from .models import blogs,favorites,ratings
from category.models import Category
@login_required
def create(request):
    if request.method == 'POST':
        form = blogsform(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('home')
    else:
        form = blogsform()
    return render(request, 'blogs/create.html', {'form': form})

def delete(request,blog_id):
    delete = blogs.objects.get(id = blog_id).delete()
    return redirect('profile')
    
def edit(request,blog_id):
    blog = blogs.objects.get(id = blog_id)
    form = blogsform(instance = blog)
    if request.method == 'POST':
        form = blogsform(request.POST,request.FILES,instance = blog)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('profile')
    return render(request,"blogs/create.html",{'form': form})

def details(request,blog_id):
    blog = blogs.objects.get(id = blog_id)
    fav = favorites.objects.filter(blog = blog)
    is_here = favorites.objects.filter(blog = blog , user = request.user)
    is_here2 = ratings.objects.filter(blog = blog , user = request.user)
    a = 0
    for i in fav:
        a += 1
    return render (request,'blogs/details.html',{'blog':blog,'i':a,'is_here':is_here,'is_here2':is_here2})

def fav(request,blog_id):
    blog = blogs.objects.get(id = blog_id)
    is_here = favorites.objects.filter(blog = blog , user = request.user)
    if is_here:
        return redirect('details',blog_id)
    else:
        favorites.objects.create(blog = blog , user = request.user)
    return redirect('details',blog_id)

def removefav(request,blog_id):
    blog = blogs.objects.get(id = blog_id)
    delete = favorites.objects.get(blog = blog , user = request.user).delete()
    return redirect('details',blog_id)

def myFav(request):
    fav = favorites.objects.filter(user = request.user)
    return render(request,"blogs/myfav.html",{'blogs': fav})

def filters(request):
    categories = Category.objects.all()
    return render(request,"blogs/category.html",{'categories':categories})

def specific(request,catid):
    categories = Category.objects.get(id = catid)
    blog = blogs.objects.filter(category = categories).order_by('-avg')
    return render(request,"blogs/specificCat.html",{'blogs':blog})


def rating(request,num,blog_id):
    blog = blogs.objects.get(id = blog_id)
    blog.rating += num
    blog.numrating += 1
    blog.avg =  blog.rating/blog.numrating
    blog.save()
    ratings.objects.create(blog = blog , user = request.user)
    return redirect('details',blog_id)