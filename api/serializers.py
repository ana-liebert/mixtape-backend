from .models import Host
from rest_framework import serializers

# class MixSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Mix
#         fields = ['id' ,'title', 'description', 'created_at', 'host', 'image', 'genre', 'soundcloudplayer', 'soundcloudlink', 'soundclouduser', 'tracklist']

class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ['name', 'bio', 'image', 'schedule']