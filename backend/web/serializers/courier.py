import random

from rest_framework import serializers

from web.models import Courier


class CourierSerializer(serializers.ModelSerializer):
    progress = serializers.CharField(default=f"{random.randint(0, 50)} км")

    class Meta:
        model = Courier
        fields = "__all__"
