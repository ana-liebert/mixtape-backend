from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from .models import Host, Mix, Genre, UserProfile 
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MixSerializer, HostSerializer, GenreSerializer, UserProfileSerializer
# RegistrationSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# class MeView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         serializer = UserSerializer(request.user)
#         return Response(serializer.data)

class HostViewSet(viewsets.ModelViewSet):  
    queryset = Host.objects.all()  
    serializer_class = HostSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]  


class MixViewSet(viewsets.ModelViewSet):
    queryset = Mix.objects.all().order_by('created_at')
    serializer_class = MixSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # def get_queryset(self):
    #     qs = super().get_queryset()

    #     # Get only contact about current authenticated user
    #     qs = qs.filter(user=self.request.user)

    #     # Add search capabilities
    #     search = self.request.query_params.get("search", None)
    #     if search:
    #         qs = qs.filter(
    #             models.Q(name__icontains=search)
    #             | models.Q(phone__icontains=search)
    #             | models.Q(email__icontains=search)
    #         )

    #     return qs

class GenreViewSet(viewsets.ModelViewSet):  
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]  

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

# class UserView(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = RegistrationSerializer