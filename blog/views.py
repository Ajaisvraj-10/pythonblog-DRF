from django.shortcuts import render
from rest_framework import viewsets
from rest_framework .permissions import AllowAny
from .models import Category,Blogs
from .serealizers import CategorySerealizer, BlogsSerealizer

# Create your views here.


class Category(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Category.objects.all()
    serializer_class = CategorySerealizer
    
    
class Blogs(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerealizer