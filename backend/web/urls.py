from django.urls import path

from web.views.courier import CourierViewSet
from web.views.hub import HubViewSet
from web.views.order import OrdersViewSet
from web.views.waybill import WaybillViewSet

urlpatterns = [
    path(
        "orders",
        OrdersViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "orders/<int:pk>",
        OrdersViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "partial_update",
            }
        ),
    ),
    path(
        "waybills",
        WaybillViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "waybills/<int:pk>",
        WaybillViewSet.as_view(
            {
                "get": "retrieve",
            }
        ),
    ),
    path(
        "couriers",
        CourierViewSet.as_view(
            {
                "get": "list",
            }
        ),
    ),
    path(
        "couriers/<int:pk>",
        CourierViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
            }
        ),
    ),
    path(
        "hubs",
        HubViewSet.as_view(
            {
                "get": "list",
            }
        ),
    ),
    path(
        "hubs/<int:pk>",
        HubViewSet.as_view(
            {
                "get": "retrieve",
            }
        ),
    ),
]
