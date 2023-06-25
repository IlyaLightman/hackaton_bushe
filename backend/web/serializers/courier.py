import random

from rest_framework import serializers

from web.models import Courier


class CourierSerializer(serializers.ModelSerializer):
    progress = serializers.CharField(
        default=f"{random.randint(0, 50)} км – 0{random.randint(0, 8)}:{random.randint(0, 60)}"
    )

    class Meta:
        model = Courier
        fields = "__all__"
