from rest_framework import serializers

from web.models import Waybill

from web.serializers.order import OrderSerializer


class WaybillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waybill
        fields = "__all__"


class CreateWaybillSerializer(serializers.Serializer):
    class OrdersSerializer(serializers.Serializer):
        order_id = serializers.IntegerField()
        order_number = serializers.IntegerField()

    courier_id = serializers.IntegerField()
    orders = OrdersSerializer(many=True)

    class Meta:
        model = Waybill


class GetWaybillSerializer(serializers.Serializer):
    courier_id = serializers.IntegerField()
    orders = OrderSerializer(many=True)
    route_url = serializers.CharField()

    class Meta:
        model = Waybill
