from django.core.management import BaseCommand

from django.core.management import BaseCommand

from web.models import Courier, Hub, Waybill, WaybillOrder


class Command(BaseCommand):
    def handle(self, *args, **options):
        for model in (
            WaybillOrder,
            Waybill,
            Courier,
            Hub,
        ):
            model.objects.filter().delete()
