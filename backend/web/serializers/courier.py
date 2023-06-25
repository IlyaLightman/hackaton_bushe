import random

from rest_framework import serializers

from web.models import Courier


class CourierSerializer(serializers.ModelSerializer):
    time_progress = serializers.CharField(default=f"0{random.randint(0, 8)}:{random.randint(0, 60)}")
    current_waybill = serializers.CharField(default="Маршрут 1")
    distance_progress = serializers.CharField(default=f"{random.randint(0, 50)} км")

    class Meta:
        model = Courier
        fields = "__all__"
