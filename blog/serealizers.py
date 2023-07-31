from rest_framework import serializers
from .models import Category,Blogs



class CategorySerealizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        

class BlogsSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'