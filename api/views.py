from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from .models import Host, Mix, Genre, UserProfile, User  
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MixSerializer, HostSerializer, GenreSerializer, UserProfileSerializer, RegistrationSerializer
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.decorators import api_view



class HostViewSet(viewsets.ModelViewSet):  
    queryset = Host.objects.all()  
    serializer_class = HostSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]  


class MixViewSet(viewsets.ModelViewSet):
    queryset = Mix.objects.all().order_by('created_at')
    serializer_class = MixSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GenreViewSet(viewsets.ModelViewSet):  
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]  

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer