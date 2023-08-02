from rest_framework import serializers
from .models import Category,Blogs,Tag



class CategorySerealizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        

class BlogsSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'
        
        
class TagSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'