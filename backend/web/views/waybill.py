from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.response import Response

from web.models import Waybill
from web.serializers.waybill import CreateWaybillSerializer, GetWaybillSerializer, WaybillSerializer


class WaybillViewSet(viewsets.ModelViewSet):
    queryset = Waybill.objects.all()

    def get_serializer_class(self):
        mapping = {
            "list": WaybillSerializer,
            "retrieve": GetWaybillSerializer,
            "create": CreateWaybillSerializer,
        }

        return mapping.get(self.action, WaybillSerializer)

    @swagger_auto_schema(
        request_body=CreateWaybillSerializer,
        responses={
            status.HTTP_201_CREATED: WaybillSerializer(),
        },
    )
    @transaction.atomic()
    def create(self, request, *args, **kwargs):
        request_serializer = CreateWaybillSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)

        waybill = self.perform_create(request_serializer)

        response_serializer = WaybillSerializer(waybill)

        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
