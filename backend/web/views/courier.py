from drf_yasg.utils import no_body, swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from web.models import Courier, Waybill, WaybillStatusChoices
from web.serializers.courier import CourierSerializer
from web.serializers.waybill import WaybillSerializer


class CourierViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()

    def get_serializer_class(self):
        mapping = {
            "list": CourierSerializer,
            "retrieve": CourierSerializer,
        }

        return mapping.get(self.action, CourierSerializer)

    @swagger_auto_schema(request_body=no_body)
    @action(
        detail=True,
        methods=["get"],
        url_path="waybill",
        url_name="waybill",
    )
    def waybill(self, request, telegram_id):
        courier = Courier.objects.get(telegram_id=telegram_id)
        waybill = Waybill.objects.get(
            courier=courier.id,
            status=WaybillStatusChoices.in_progress,
        )

        waybill_serialized = WaybillSerializer(waybill)
        return Response(waybill_serialized.data)
