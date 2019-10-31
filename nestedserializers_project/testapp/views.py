from django.shortcuts import render
from rest_framework import generics
from testapp.models import Author,Book
from testapp.serializers import AuthorSerializer,BookSerializer
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import requests
import json
from django.http import HttpResponse
from rest_framework import viewsets

class authorlist(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticated,]


class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

class AuthorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def index(request):
    url = 'https://jsonplaceholder.typicode.com/'
    res= requests.get(url+'posts')
    print(res)
    data = res.json()
    json_data = json.dumps(data)

    return HttpResponse(json_data,content_type='application/json')

class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


