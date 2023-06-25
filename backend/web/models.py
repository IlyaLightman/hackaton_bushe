import enum

import django.utils.timezone
from django.db import models


class OrderStatusChoices(models.TextChoices):
    created = "created"
    picked = "picked"
    canceled = "canceled"
    delivered = "delivered"


class OrderHistoryEventChoices(models.TextChoices):
    status_changed = "status_changed"


class WaybillStatusChoices(models.TextChoices):
    created = "created"
    appointed = "appointed"
    in_progress = "in_progress"
    completed = "completed"


class CourierStatusChoices(models.TextChoices):
    free = "free"
    busy = "busy"


class OrderEventEnum(enum.StrEnum):
    created = enum.auto()
    changed = enum.auto()


class Hub(models.Model):
    name = models.TextField()
    logo = models.TextField(null=True)
    address_lat = models.FloatField()
    address_lon = models.FloatField()
    address_string = models.TextField()


class Courier(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=CourierStatusChoices.choices)
    telegram_id = models.CharField(max_length=255, null=True)
    hub = models.ForeignKey("Hub", on_delete=models.RESTRICT)


class Order(models.Model):
    products = models.JSONField()
    status = models.CharField(max_length=255, choices=OrderStatusChoices.choices)
    weight = models.FloatField()
    address_string = models.CharField(max_length=255)
    address_lat = models.FloatField()
    address_lon = models.FloatField()
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=255)


class OrderHistory(models.Model):
    order = models.ForeignKey("Order", on_delete=models.RESTRICT)
    event = models.CharField(max_length=255, choices=OrderHistoryEventChoices.choices)
    value = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=django.utils.timezone.now)


class Waybill(models.Model):
    status = models.CharField(max_length=255, choices=WaybillStatusChoices.choices)
    courier = models.ForeignKey("Courier", on_delete=models.RESTRICT, null=True)
    route_url = models.TextField(null=True)


class WaybillOrder(models.Model):
    waybill = models.ForeignKey("Waybill", on_delete=models.RESTRICT, related_name="orders")
    order = models.ForeignKey("Order", on_delete=models.RESTRICT)
    order_number = models.IntegerField()
