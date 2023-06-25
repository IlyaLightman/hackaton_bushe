from django.core.management import BaseCommand
from django.db import connection

from web.models import Courier, Hub, Order, OrderHistory, Waybill, WaybillOrder


class Command(BaseCommand):
    def handle(self, *args, **options):
        for model in (
            WaybillOrder,
            Waybill,
            OrderHistory,
            Order,
            Courier,
            Hub,
        ):
            model.objects.filter().delete()

        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE web_courier_id_seq RESTART;")
            cursor.execute("ALTER SEQUENCE web_hub_id_seq RESTART;")
            cursor.execute("ALTER SEQUENCE web_order_id_seq RESTART;")
            cursor.execute("ALTER SEQUENCE web_orderhistory_id_seq RESTART;")
            cursor.execute("ALTER SEQUENCE web_waybill_id_seq RESTART;")
            cursor.execute("ALTER SEQUENCE web_waybillorder_id_seq RESTART;")
