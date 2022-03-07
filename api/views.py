from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse

# Create your views here.

class Home(View):
    def get(self, request, *args, **kwargs):
        
        return HttpResponse("Mixtape Homepage")


class DiscoverIndex(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Discover page")

class MixDetail(View):
    def get(self, request, id, *args, **kwargs):
        print("args are", args)
        print("kwargs are", kwargs)
        # ^kwards are the param typed into the url
        return HttpResponse(f"<h1> Hello {id} </h1>")