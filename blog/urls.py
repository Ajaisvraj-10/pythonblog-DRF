from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Category, Blogs,Tag


router = DefaultRouter()
router.register(r'categories',Category)
router.register(r'blogs',Blogs)
router.register(r'tags',Tag)

urlpatterns = [
    
    path('',include(router.urls)),
    
]