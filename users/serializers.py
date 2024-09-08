from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import User

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields =('username', 'first_name', 'last_name', 'phone_number', 'password')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    

    
    