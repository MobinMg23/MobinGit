from django.contrib import admin
from django.urls import path, include
from .views import HomeAPIView, AddCarAPIView

urlpatterns = [
    path('home/', HomeAPIView.as_view(), name='home'),
    path('add-car/', AddCarAPIView.as_view(), name='add-car'),
]