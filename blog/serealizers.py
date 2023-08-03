from rest_framework import serializers
from .models import Category,Blogs,Tag



class CategorySerealizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        
class BlogsSerealizer(serializers.ModelSerializer):
    tag_names = serializers.SerializerMethodField()  # Add this line

    class Meta:
        model = Blogs
        fields = '__all__'

    def get_tag_names(self, obj):  # Update method name to match field name
        return list(obj.tags.all().values_list('name', flat=True))

        
        
class TagSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        