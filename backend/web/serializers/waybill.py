from rest_framework import serializers

from web.models import Waybill


class WaybillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waybill
        fields = "__all__"


class CreateWaybillSerializer(serializers.Serializer):
    class OrdersSerializer(serializers.Serializer):
        order_id = serializers.IntegerField()
        order_number = serializers.IntegerField()

    courier_id = serializers.IntegerField()
    orders = OrdersSerializer()

    class Meta:
        model = Waybill
