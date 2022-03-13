from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from .models import Host, Mix, Genre, UserProfile 
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MixSerializer, HostSerializer, GenreSerializer, UserProfileSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response




class HostViewSet(viewsets.ModelViewSet):  
    queryset = Host.objects.all()  
    serializer_class = HostSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]  


class MixViewSet(viewsets.ModelViewSet):
    queryset = Mix.objects.all().order_by('created_at')
    serializer_class = MixSerializer

    def create(self, request, *args, **kwargs):
    print request.data
    return super(MixViewSet, self).create(request, *args, **kwargs)


class GenreViewSet(viewsets.ModelViewSet):  
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]  

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

