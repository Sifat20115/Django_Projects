from django.db import models
from category.models import Category
from django.contrib.auth.models import User
# Create your models here.
class blogs(models.Model):
    blog_title      = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    images          = models.ImageField(upload_to='photos/chobi',blank=True)
    description     = models.TextField(max_length=5000, blank=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(null=True, default=0)
    numrating = models.IntegerField(null=True, default=0)
    avg = models.IntegerField(null=True, default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.blog_title

class favorites(models.Model):
    blog = models.ForeignKey(blogs,on_delete=models.CASCADE,null=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    
class ratings(models.Model):
    blog = models.ForeignKey(blogs,on_delete=models.CASCADE,null=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False)