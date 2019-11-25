from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from MyApp.serializers import UserSerializer, GroupSerializer, BooksSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from MyApp.models import Books

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@api_view(['GET', 'POST'])
def book_list(request):
    """
    List all code Books, or create a new Book.
    """
    if request.method == 'GET':
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True) #many=True por ser una lista de modelos y no un único modelo
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
