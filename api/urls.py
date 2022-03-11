# from django.urls import path
# from rest_framework import routers
# from api import views
# from django.contrib.auth import views as auth_views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )


# router = routers.DefaultRouter()
# router.register(r'mixes', views.MixViewSet, 'mixes'),
# router.register(r'hosts', views.HostViewSet, 'hosts'),
# router.register(r'discover', views.GenreViewSet, 'discover'),
# router.register(r'profile', views.UserProfileViewSet, 'profile'),
# router.register(r'register', views.UserView, 'register'),

# urlpatterns = [
#     path('mixtape/', include(router.urls)),
#     path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]