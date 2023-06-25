import random

from rest_framework import serializers

from web.models import Courier, Waybill


class CourierSerializer(serializers.ModelSerializer):
    time_progress = serializers.CharField(default=f"0{random.randint(0, 8)}:{random.randint(0, 60)}")
    distance_progress = serializers.CharField(default=f"{random.randint(0, 50)} км")
    waybill = serializers.CharField()

    class Meta:
        model = Courier
        fields = "__all__"
