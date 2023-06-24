from rest_framework import viewsets

from web.models import Courier
from web.serializers.courier import CourierSerializer


class CourierViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()

    def get_serializer_class(self):
        mapping = {
            "list": CourierSerializer,
            "retrieve": CourierSerializer,
        }

        return mapping.get(self.action, CourierSerializer)
