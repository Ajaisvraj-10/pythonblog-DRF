from django.shortcuts import render
from rest_framework import viewsets
from .models import Category,Blogs
from .serealizers import CategorySerealizer, BlogsSerealizer

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerealizer
    
    
class BlogsViewSet(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerealizer