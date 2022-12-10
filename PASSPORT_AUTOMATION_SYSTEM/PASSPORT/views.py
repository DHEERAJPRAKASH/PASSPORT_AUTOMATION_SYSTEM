from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import PassportDatabase
from .serializers import PassportSerializer,UserSerializer
from django.http import JsonResponse
from rest_framework import status,generics,mixins,viewsets
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view,APIView,permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,SAFE_METHODS,BasePermission
from django.contrib.auth.models import User

class PassportViewSet(viewsets.ModelViewSet):
    queryset = PassportDatabase.objects.all()
    serializer_class = PassportSerializer
  
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer




