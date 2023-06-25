from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.response import Response

from web.models import Order
from web.serializers.order import (
    CreateOrderSerializer,
    OrderSerializer,
    UpdateOrderSerializer,
)


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @swagger_auto_schema(
        request_body=CreateOrderSerializer,
        responses={
            status.HTTP_201_CREATED: OrderSerializer(),
        },
    )
    def create(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order = self.perform_create(serializer)

        result = OrderSerializer(order)
        return Response(data=result.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        request_body=UpdateOrderSerializer,
        responses={
            status.HTTP_200_OK: OrderSerializer(),
        },
    )
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = UpdateOrderSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        order = self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        result = OrderSerializer(order)
        return Response(result.data)

    @swagger_auto_schema(
        request_body=UpdateOrderSerializer,
        responses={
            status.HTTP_200_OK: OrderSerializer(),
        },
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
