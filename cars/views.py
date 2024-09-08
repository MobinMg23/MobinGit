from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.contrib import messages
from .models import Car
from .forms import CarForm
from users.models import User


class HomeAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'home.html'
    def get(self, request):
        cars = Car.objects.all()
        return Response({
            'cars': cars
        })


class AddCarAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'add_car.html'
    permission_classes = [IsAuthenticated, ]
    
    
    def get(self, request):
        form = CarForm()
        return Response({"form": form})
        
    def post(self, request):
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.car_from = self.request.user
            car.save()
            messages.success(request, ('add is seccusfuly'))
            return redirect('/home/')
        
        return Response({'form': form})
    




