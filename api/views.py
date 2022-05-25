from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from .models import Host, Mix, Genre, UserProfile 
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MixSerializer, HostSerializer, GenreSerializer, UserProfileSerializer
from users.serializers import RegisterUserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import filters


class HostViewSet(viewsets.ModelViewSet):  
    queryset = Host.objects.all()  
    serializer_class = HostSerializer


class MixViewSet(viewsets.ModelViewSet):
    queryset = Mix.objects.all().order_by('-created_at')
    serializer_class = MixSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'host']

class MixSearch(generics.ListAPIView):
    queryset = Mix.objects.all()
    serializer_class = MixSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class GenreViewSet(viewsets.ModelViewSet):  
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer 



class MixList(generics.ListAPIView):
    queryset = Mix.objects.all()
    serializer_class = MixSerializer