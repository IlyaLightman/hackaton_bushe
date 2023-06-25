from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters
from web.models import Courier, Waybill, WaybillStatusChoices
from web.serializers.courier import CourierSerializer
from web.serializers.waybill import WaybillSerializer


class CourierFilter(filters.FilterSet):
    hub = filters.NumberFilter(field_name="hub__id")

    class Meta:
        model = Courier
        fields = ["hub"]


class CourierViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CourierFilter

    def get_serializer_class(self):
        mapping = {
            "list": CourierSerializer,
            "retrieve": CourierSerializer,
            "waybill": WaybillSerializer,
        }

        return mapping.get(self.action, CourierSerializer)

    @swagger_auto_schema()
    @action(
        detail=True,
        methods=["get"],
        url_path="waybill",
        url_name="waybill",
    )
    def waybill(self, request, telegram_id):
        courier = Courier.objects.get(telegram_id=telegram_id)
        try:
            waybill = Waybill.objects.get(
                courier=courier.id,
                status=WaybillStatusChoices.in_progress,
            )
        except ObjectDoesNotExist:
            raise Http404

        waybill_serialized = WaybillSerializer(waybill)
        return Response(waybill_serialized.data)
