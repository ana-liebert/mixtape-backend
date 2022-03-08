from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'mixes', views.MixViewSet),

# router.register(r'hosts', views.HostViewSet),
# router.register(r'genres', views.GenreViewSet),


urlpatterns = [
    # path(r'^api/', include(router.urls)),

    # path('home/', views.MixViewSet.as_view()),
    # path('home/', views.MixViewSet.as_view({'get': 'list'}), name="home"),
    # path('hosts/', views.HostViewSet.as_view({'get': 'list'}), name="host"),
    # path('discover/', views.GenreViewSet.as_view({'get': 'list'}), name="discover"),
    # path('discover/', views.Home.as_view(), name="landing"),
    # path('mixdetail/<str:pk/>', views.Home.as_view(), name="landing"),
    # path('mix-create/', views.Home.as_view(), name="landing"),
    # path('mix-update/<str:pk>/', views.Home.as_view(), name="landing"),
    # path('mix-delete/<str:pk>/', views.Home.as_view(), name="landing"),
]

# urlpatterns = format_suffix_patterns(urlpatterns)