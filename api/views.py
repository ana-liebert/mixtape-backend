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



# The SearchFilter class will only be applied if the view has a search_fields attribute set. The search_fields attribute should be a list of names of text type fields on the model, such as CharField or TextField.

# from rest_framework import filters

# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['username', 'email']
# This will allow the client to filter the items in the list by making queries such as:

# http://example.com/api/users?search=russell


class HostViewSet(viewsets.ModelViewSet):  
    queryset = Host.objects.all()  
    serializer_class = HostSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]  


# class MixList(generics.ListCreateAPIView):
#     queryset = Mix.objects.all().order_by('created_at')
#     serializer_class = MixSerializer
#     pass

# these generic view classes detirmine what you can do on that view endpoint 
# class MixDetail(generics.RetrieveDestroyAPIView):
#     queryset = Mix.objects.all().order_by('created_at')
#     serializer_class = MixSerializer
#     pass



# class MixView(generics.ListAPIView):
#     queryset = Mix.objects.all().order_by('created_at')
#     serializer_class = MixSerializer
#     permission_classes = [permissions.AllowAny]  
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title', 'host']

class MixViewSet(viewsets.ModelViewSet):
    queryset = Mix.objects.all().order_by('created_at')
    serializer_class = MixSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'host']

class MixSearch(generics.ListAPIView):
    queryset = Mix.objects.all()
    serializer_class = MixSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    # http://localhost:8000/search/custom?search=mixtest




class GenreViewSet(viewsets.ModelViewSet):  
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer 


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    # permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user_object = UserProfile.objects.get()

        data = request.data
        user_object.user = data["user"]
        user_object.favorites = data["mixes"] # or maybe mixes...?

        user_object.save()

        serializer = UserProfileSerializer
        return Response(serializer.data)


# class UserProfileList(generics.ListAPIView):

#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer

# class UserProfileIndvList(generics.ListAPIView):

#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer

# class UserProfileUpdate(generics.UpdateAPIView):

#     # def put(self, request, *args, **kwargs):
#     #     user_object = UserProfile.objects.get()

#     #     data = request.data
#     #     user_object.user = data["user"]
#     #     user_object.favorites = data["favorites"] # or maybe mixes...?

#     #     user_object.save()

#     #     serializer = UserProfileSerializer
#     #     return Response(serializer.data)

#     serializer_class = UserProfileSerializer
#     queryset = UserProfile.objects.all()

