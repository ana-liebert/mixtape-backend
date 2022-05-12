from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from .models import Host, Mix, Genre, UserProfile 
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MixSerializer, HostSerializer, GenreSerializer, UserProfileSerializer
from users.models import NewUser
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def put(self, request, *args, **kwargs):
        user_object = UserProfile.objects.get()

        data = request.data
        user_object.user = data["user"]
        user_object.favorites = data["mixes"]

        user_object.save()

        serializer = UserProfileSerializer
        return Response(serializer.data)

