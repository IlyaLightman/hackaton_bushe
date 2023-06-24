from django.db import transaction
from rest_framework import viewsets

from web.models import Order, OrderEventEnum, OrderHistory
from web.serializers.order import (
    CreateOrderSerializer,
    OrderSerializer,
    UpdateOrderSerializer,
)


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        mapping = {
            "list": OrderSerializer,
            "retrieve": OrderSerializer,
            "create": CreateOrderSerializer,
            "update": UpdateOrderSerializer,
            "partial_update": UpdateOrderSerializer,
        }

        return mapping.get(self.action, OrderSerializer)
