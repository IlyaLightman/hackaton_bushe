from django.core.management import BaseCommand

from django.core.management import BaseCommand

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
