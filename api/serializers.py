from .models import Host, Mix, Genre, UserProfile
# User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         exclude = ('password', )


# class RegistrationSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

#     class Meta:
#         model = User
#         fields = ['email', 'username', 'password', 'password2']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }
#     # override the save method to validate
#     def save(self):
#         user = User(
#             email=self.validated_data['email'],
#             username=self.validated_data['username'],
#         )
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']

#         if password != password2:
#             raise serializers.ValidationError({'password': 'Passwords must match.'})
#         user.set_password(password)
#         user.save()
#         return user



class HostSerializer(serializers.ModelSerializer):
    hosts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Host
        fields = ['id', 'name', 'bio', 'image', 'schedule', 'hosts']


class MixSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)
    class Meta:
        model = Mix
        fields = ['id' ,'title', 'description', 'created_at', 'host', 'genre', 'image', 'soundcloudplayer', 'soundcloudlink', 'soundclouduser', 'creator']

class GenreSerializer(serializers.ModelSerializer):
    mix_list = MixSerializer(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = ['id', 'name', 'mix_list']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'favorites']
