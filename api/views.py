from django.shortcuts import render
from django.views import View 
from django.http import JsonResponse

# Create your views here.

class Home(View):
    def get(self, request):
        return JsonResponse("Mixtape Homepage", safe=False)


class Discover(View):
    def get(self, request):
        return JsonResponse("Discover page", safe=False)

# JON HASSELL 
# Toucan Ocean
# KAMURAN AKKOR 
# Ikimiz Bir Fidaniz
# ESMERAY 
# Ayrılık Olsa Bile
# BIG THIEF 
# Blurred View
# ESG 
# Moody
# MUSTAFA SANDAL 
# Jest Oldu
# SHAMIR 
# On The Regular
# GÜLŞEN 
# Be Adam
# LÉA SEN
# Hyasynth
# P J HARVEY 
# Rid Of Me
# KEIYAA 
# Forreal???
# DUENDITA
# Bury Me
# MAZHAR VE FUAT 
# Adımız Miskindir Bizim
# KADER 
# Adamım
# ÖZDEMIR ERDOĞAN 
# Gurbet
# NEŞE KARABÖCEK 
# Kemanci
