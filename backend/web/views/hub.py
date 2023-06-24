from rest_framework import generics, viewsets

from web.models import Hub
from web.serializers.hub import HubSerializer


class HubViewSet(viewsets.ModelViewSet):
    queryset = Hub.objects.all()
    serializer_class = HubSerializer
