from rest_framework import viewsets

from web.models import Waybill
from web.serializers.waybill import CreateWaybillSerializer, WaybillSerializer


class WaybillViewSet(viewsets.GenericViewSet):
    queryset = Waybill.objects.all()

    def get_serializer_class(self):
        mapping = {
            "list": WaybillSerializer,
            "retrieve": WaybillSerializer,
            "create": CreateWaybillSerializer,
        }

        return mapping.get(self.action, WaybillSerializer)