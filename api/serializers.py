from .models import Host, Mix, Genre, UserProfile
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class HostSerializer(serializers.ModelSerializer):
    hosts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Host
        fields = ['id', 'name', 'bio', 'image', 'schedule', 'hosts']


class MixSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)
    # For many-to-many relationships set() accepts a list of either model instances or field values, normally primary keys, as the objs argument.
    # genre = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=False,
    #     slug_field='genre_name',
    #     queryset=Genre.objects.all()
    # )

    class Meta:
        model = Mix
        fields = ['id' ,'title', 'description', 'created_at', 'host', 'genre', 'image', 'soundcloudplayer', 'creator']

class GenreSerializer(serializers.ModelSerializer):
    mix_list = MixSerializer(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = ['id', 'name', 'mix_list']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'favorites']
