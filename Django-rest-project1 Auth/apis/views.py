from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


class GanreListAPIView(ListAPIView):
    queryset = Ganre.objects.all()
    serializer_class = GanreSerializer 
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_fields = ['ganre_name',] 
    search_fields = ['ganre_name',]
    permission_classes = [IsAuthenticated]

class GanreCreateAPIView(CreateAPIView):
    queryset = Ganre.objects.all()
    serializer_class = GanreSerializer
    permission_classes = [IsAuthenticated]


class GanreRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Ganre.objects.all()
    serializer_class = GanreSerializer
    permission_classes = [IsAuthenticated]



class GanreDestroyAPIView(DestroyAPIView):
    queryset = Ganre.objects.all()
    permission_classes = [IsAuthenticated]



class AuthorListAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer 
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_fields = ['f_name','l_name',] 
    search_fields = ['f_name',]
    permission_classes = [IsAuthenticated]

    
class AuthorCreateAPIView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]


class AuthorRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]



class AuthorDestroyAPIView(DestroyAPIView):
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated]


class BooksListAPIView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer 
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_fields = ['name_book','author','ganre',"date_out"] 
    ordering_fields = ['price', 'page'] 
    search_fields = ['name_book',]
    permission_classes = [IsAuthenticated]


class BooksRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsAuthenticated]


class BooksDestroyAPIView(DestroyAPIView):
    queryset = Books.objects.all()    
    permission_classes = [IsAuthenticated]

class BooksCreateAPIView(CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsAuthenticated]



class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer 
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_fields = ['book','username',] 
    ordering_fields = ['created_at', 'total_price',"count"] 
    search_fields = ['username',]
    permission_classes = [IsAuthenticated]

class OrderRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

class OrderDestroyAPIView(DestroyAPIView):
    queryset = Order.objects.all()    
    permission_classes = [IsAuthenticated]

class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
