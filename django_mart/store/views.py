from django.shortcuts import render, get_object_or_404, redirect
from store.models import Product
from category.models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def store(request, category_slug = None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
        
        
        
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
        
    
    category = Category.objects.all()
    context = {'products' : paged_product, 'category' : category}
    return render(request,'store/store.html',context)





def product_detail(request,category_slug,product_slug):
    single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    return render(request,'store/product_details.html',{'single_product':single_product})