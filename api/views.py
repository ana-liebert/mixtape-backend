from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from .models import Host, Mix  
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import HostSerializer, MixSerializer 


# Create your views here.

# class Home(View):
#     def get(self, request, *args, **kwargs):
        
#         return HttpResponse("Mixtape Homepage")


# class DiscoverIndex(View):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse("Discover page")

# class MixDetail(View):
#     def get(self, request, id, *args, **kwargs):
#         print("args are", args)
#         print("kwargs are", kwargs)
#         # ^kwards are the param typed into the url
#         return HttpResponse(f"<h1> Hello {id} </h1>")


class HostViewSet(viewsets.ModelViewSet):  
    queryset = Host.objects.all()  
    serializer_class = HostSerializer
    permission_classes = [permissions.IsAuthenticated]  

class MixViewSet(viewsets.ModelViewSet):  
    queryset = Mix.objects.all().order_by('created_at')
    serializer_class = MixSerializer
    permission_classes = [permissions.IsAuthenticated]  