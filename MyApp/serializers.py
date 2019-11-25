from django.contrib.auth.models import User, Group
from rest_framework import serializers
from MyApp.models import Books

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'type', 'author', 'creation_date', 'number_of_pages','user','borrow_date']
