import datetime
import enum

from django.db import models


class OrderStatusEnum(models.TextChoices):
    created = "created"
    picked = "picked"
    canceled = "canceled"
    delivered = "delivered"


class OrderEventEnum(enum.StrEnum):
    created = enum.auto()
    changed = enum.auto()


class Hub(models.Model):
    name = models.CharField(max_length=255)
    address_lat = models.FloatField()
    address_lon = models.FloatField()
    address_string = models.CharField(max_length=255)


class HubWorkHours(models.Model):
    hub = models.ForeignKey("Hub", on_delete=models.RESTRICT)
    weekday = models.IntegerField()
    start = models.TimeField()
    end = models.TimeField()


class Courier(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)


class CourierWorkHours(models.Model):
    courier = models.ForeignKey("Courier", on_delete=models.RESTRICT)
    weekday = models.IntegerField()
    start = models.TimeField()
    end = models.TimeField()


class Order(models.Model):
    products = models.JSONField()
    status = models.CharField(max_length=255, choices=OrderStatusEnum.choices)
    weight = models.FloatField()
    address_string = models.CharField(max_length=255)
    address_lat = models.FloatField()
    address_lon = models.FloatField()
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=255)


class OrderHistory(models.Model):
    order = models.ForeignKey("Order", on_delete=models.RESTRICT)
    event = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=datetime.datetime.utcnow)


class Waybill(models.Model):
    courier = models.ForeignKey("Courier", on_delete=models.RESTRICT, null=True)
    route_url = models.TextField()


class WaybillOrder(models.Model):
    waybill = models.ForeignKey("Waybill", on_delete=models.RESTRICT)
    order = models.ForeignKey("Order", on_delete=models.RESTRICT)
    number = models.IntegerField()
