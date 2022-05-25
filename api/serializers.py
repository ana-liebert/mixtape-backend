from .models import Host, Mix, Genre, UserProfile
from users.serializers import RegisterUserSerializer
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class HostSerializer(serializers.ModelSerializer):
    hosts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Host
        fields = ['id', 'name', 'bio', 'image', 'schedule', 'hosts']


class MixSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)
    creator = RegisterUserSerializer
    
    class Meta:
        model = Mix
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    mix_list = MixSerializer(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = ['id', 'name', 'mix_list']

class UserProfileSerializer(serializers.ModelSerializer):
    user = RegisterUserSerializer(read_only=True)
    posts = MixSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'
