"""mixtape_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from api import views
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




router = routers.DefaultRouter()
router.register(r'mixes', views.MixViewSet, 'mixes'),
router.register(r'hosts', views.HostViewSet, 'hosts'),
router.register(r'discover', views.GenreViewSet, 'discover'),
router.register(r'profile', views.UserProfileViewSet, 'profile'),



urlpatterns = [
    path('admin/', admin.site.urls),
    path('mixtape/', include(router.urls)),
    path('user/', include('users.urls', namespace='users')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('search/', views.MixSearch.as_view(), name="listcreate"),
    # path('profile/', views.UserProfileList.as_view(), name="profile"),
    # path('profile/<int:pk>/', views.UserProfileUpdate.as_view(), name="profile"),
    # path('profile/<int:pk>/', views.UserProfileIndvList.as_view(), name="profile"),
    re_path(r'^(?P<path>.*)/$', views.MixViewSet.as_view({'get': 'list'})),
    path('/', views.MixViewSet.as_view({'get': 'list'})),
    
]
