from rest_framework import serializers
from .models import PassportDatabase
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

#MODEL SERIALZIER
class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassportDatabase
        fields =['id','Name','FatherName','DateOfBirth','Address','PermanentAddress','PhoneNumber','PanNo','EmailId','ApplicationNo','Username','Password','R_admin_verified','Police_verified','Passport_admin_verified']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {'password':{
            'write_only':True,
            'required':True }}
            
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
        
