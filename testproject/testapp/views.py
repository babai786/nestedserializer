from django.shortcuts import render

# Create your views here.

from rest_framework.generics import  RetrieveUpdateDestroyAPIView,ListCreateAPIView
from testapp.serializers import  AuthorSerializer,BookSerializer
from testapp.models import Author,Book

class AuthorListView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



