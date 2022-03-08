from django.urls import path, include
from . import views
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'hosts', views.HostViewSet),
router.register(r'mixes', views.MixViewSet),

urlpatterns = [
    path('host/', views.HostViewSet.as_view({'get': 'list'}), name="host"),
    path('discover/', views.MixViewSet.as_view({'get': 'list'}), name="discover"),
    # path('', views.Home.as_view(), name="home"),
    # path('discover/<int:id>', views.MixDetail.as_view(), name="mixdetail"),
]