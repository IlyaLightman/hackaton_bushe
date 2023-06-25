from rest_framework import serializers

from web.models import Order


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class CreateOrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "weight",
            "products",
            "address_lat",
            "address_lon",
            "address_string",
        )


class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("status",)


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    waybill = serializers.CharField()

    class Meta:
        model = Order
        fields = "__all__"
