from .models import Host, Mix, Genre, UserProfile
from rest_framework import serializers



class HostSerializer(serializers.HyperlinkedModelSerializer):
    hosts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Host
        fields = ['id', 'name', 'bio', 'image', 'schedule', 'hosts']


class MixSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mix
        fields = ['id' ,'title', 'description', 'created_at', 'host', 'genre', 'image', 'soundcloudplayer', 'soundcloudlink', 'soundclouduser', 'tracklist']

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'favorites']
