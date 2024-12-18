from django.contrib import admin
from django.urls import path,include
from .views import PassportViewSet,UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Passport',PassportViewSet, basename='Passport')
router.register('users',UserViewSet)
urlpatterns = [
    path('api/',include(router.urls)),
]
