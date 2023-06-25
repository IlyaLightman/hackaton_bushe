from rest_framework import viewsets

from web.models import Waybill
from web.serializers.waybill import CreateWaybillSerializer, WaybillSerializer,GetWaybillSerializer

class WaybillViewSet(viewsets.GenericViewSet):
    queryset = Waybill.objects.all()

    def get_serializer_class(self):
        mapping = {
            "list": WaybillSerializer,
            "retrieve": GetWaybillSerializer,
            "create": CreateWaybillSerializer,
        }

        return mapping.get(self.action, WaybillSerializer)
