from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BlogsViewSet


router = DefaultRouter()
router.register(r'categories',CategoryViewSet)
router.register(r'blogs',BlogsViewSet)

urlpatterns = [
    
    path('',include(router.urls)),
    
]