from rest_framework import serializers

from web.models import Hub


class HubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hub
        fields = "__all__"
