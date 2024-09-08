from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib import messages
from .serializers import SignUpSerializer
from .models import User
from .forms import LoginForm
from cars.models import Car
    
    
class SignUpAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny, ]
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'signup.html'
    serializer_class = SignUpSerializer
    
    def get(self, request):
        serializer = self.get_serializer()
        return Response({'serializer': serializer})
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})

        serializer.save()
        messages.success(request, ('user created'))
        return redirect('/login/')
    

class LoginAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = "index.html"
    
    def get(self, request):
        form = LoginForm()
        return Response({'form': form})
    
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(request, username=username, password=password)
        if not user:
            messages.success(request, ('data is not valid'))
            return redirect('/login/')
        dj_login(request, user)
        messages.success(request, ('user is login'))        
        return redirect('/home/')
        

class LogoutAPIView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            dj_logout(request)
            messages.success(request, ('user logout'))
            return redirect('/home/')


class UserPostAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'user_post.html'

    def get(self, request):
        posts = Car.objects.filter(car_from__username = request.user.username)
        return Response({'posts': posts})
    

        

            
            
        
        


    


    


