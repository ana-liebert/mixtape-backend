from .models import Host, Mix
from rest_framework import serializers


class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ['name', 'bio', 'image', 'schedule']


class MixSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mix
        fields = ['id' ,'title', 'description', 'created_at', 'host_id', 'image', 'soundcloudplayer', 'soundcloudlink', 'soundclouduser', 'tracklist']