from rest_framework import serializers

from web.models import Waybill, WaybillOrder, WaybillStatusChoices
from web.serializers.courier import CourierSerializer
from web.serializers.order import OrderSerializer


class WaybillOrderSerializer(serializers.Serializer):
    order = OrderSerializer()
    order_number = serializers.IntegerField()


class WaybillSerializer(serializers.ModelSerializer):
    orders = WaybillOrderSerializer(many=True)
    courier = CourierSerializer()

    class Meta:
        model = Waybill
        fields = "__all__"


class CreateWaybillOrderSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    order_number = serializers.IntegerField()


class CreateWaybillSerializer(serializers.Serializer):
    orders = CreateWaybillOrderSerializer(many=True)

    def create(self, validated_data):
        waybill_instance = Waybill.objects.create(status=WaybillStatusChoices.created, courier=None)

        WaybillOrder.objects.bulk_create(
            WaybillOrder(
                waybill=waybill_instance,
                order_id=order["order_id"],
                order_number=order["order_number"],
            )
            for order in validated_data["orders"]
        )

        return waybill_instance

    class Meta:
        model = Waybill


class GetWaybillSerializer(serializers.Serializer):
    courier_id = serializers.IntegerField()
    orders = OrderSerializer(many=True)
    route_url = serializers.CharField()

    class Meta:
        model = Waybill
