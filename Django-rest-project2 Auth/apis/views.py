from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import *
from .serealizers import *

# Create your views here.

class CarListAPIView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer 
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_fields = ['car_name', 'created_at',"company_id"] 
    ordering_fields = ['price', 'speed'] 
    search_fields = ['car_name', 'color', 'probeg']
    
class CarCreateAPIView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer



class CompanyListAPIView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_fields = ['name_company', 'created_at'] 
    ordering_fields = ['profit', 'created_at'] 
    search_fields = ['name_company', 'profit', 'date_birth']

class CompanyCreateAPIView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
