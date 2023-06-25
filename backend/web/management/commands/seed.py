from typing import Optional

import mimesis

from django.core.management import BaseCommand

from web.models import Courier, CourierStatusChoices, Hub, Order, OrderStatusChoices


class Faker(mimesis.Generic):
    address: Optional[mimesis.Address]
    person: Optional[mimesis.Person]
    text: Optional[mimesis.Text]


class Command(BaseCommand):
    faker = Faker(locale=mimesis.locales.Locale.RU)

    def handle(self, *args, **options):
        self._create_hubs()
        self._create_couriers()
        self._create_orders()

    def _create_hubs(self):
        hubs_logos = [
            "https://avatars.mds.yandex.net/get-altay/2812564/2a0000017089a44e442252f100040cd2767b/XXL",
            "https://avatars.mds.yandex.net/get-altay/2056672/2a0000016d776d189012e5d3c299ad8fcb78/XXXL",
            "https://avatars.mds.yandex.net/get-altay/2006845/2a0000016e7eccb5c9fae5ac01e3e39b5930/XXXL",
            "https://avatars.mds.yandex.net/get-altay/4435487/2a000001779493f164fac51f48e0f764bf05/XXXL",
        ]

        Hub.objects.bulk_create(
            Hub(
                name=f"Хаб №{i + 1}",
                logo=logo,
                address_string=self.faker.address.address(),
                address_lat=self.faker.address.latitude(),
                address_lon=self.faker.address.longitude(),
            )
            for i, logo in enumerate(hubs_logos)
        )

    def _create_couriers(self):
        hub = Hub.objects.all().first()
        Courier.objects.bulk_create(
            Courier(
                hub=hub,
                name=self.faker.person.full_name(),
                status=self.faker.random.choice(CourierStatusChoices.names),
            )
            for _ in range(50)
        )

    def _create_orders(self):
        Order.objects.bulk_create(
            Order(
                products=[{"id": 1, "name": "Булочка"}, {"id": 2, "name": "Водичка"}],
                status=OrderStatusChoices.created,
                weight=self.faker.random.randint(1, 10),
                address_string=self.faker.address.address(),
                address_lat=self.faker.address.latitude(),
                address_lon=self.faker.address.longitude(),
                customer_name=self.faker.person.name(),
                customer_phone=self.faker.person.phone_number(),
            )
            for _ in range(50)
        )
