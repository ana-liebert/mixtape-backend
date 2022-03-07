from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('discover/', views.DiscoverIndex.as_view(), name="discover"),
    path('discover/<int:id>', views.MixDetail.as_view(), name="mixdetail"),
]