from django.urls import path
from .views import CustomUserCreate, BlacklistTokenView, UserViewSet
from users import views

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name="create_user"),
    path('users/', views.UserViewSet.as_view({'get': 'list'}), name="create_user"),
    path('logout/blacklist/', BlacklistTokenView.as_view(),
        name='blacklist')
]
