from django.contrib import admin
from .models import Category,Blogs,Tag
# Register your models here.
admin.site.register(Category)
admin.site.register(Blogs)
admin.site.register(Tag)