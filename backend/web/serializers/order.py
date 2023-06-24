from rest_framework import serializers

from web.models import Order


class CreateOrderSerializer(serializers.ModelSerializer):
    class ProductSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()

    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ("products", "weight", "address_lat", "address_lon", "address_string")


class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("status",)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
