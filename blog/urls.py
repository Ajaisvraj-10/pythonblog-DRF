from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Category, Blogs


router = DefaultRouter()
router.register(r'categories',Category)
router.register(r'blogs',Blogs)

urlpatterns = [
    
    path('',include(router.urls)),
    
]