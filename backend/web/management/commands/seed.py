from typing import Optional

import mimesis

from django.core.management import BaseCommand

from web.models import Courier, CourierStatusChoices, Hub


class Faker(mimesis.Generic):
    address: Optional[mimesis.Address]
    person: Optional[mimesis.Person]
    text: Optional[mimesis.Text]


class Command(BaseCommand):
    faker = Faker(locale=mimesis.locales.Locale.RU)

    def handle(self, *args, **options):
        self._create_hubs()
        self._create_couriers()

    def _create_hubs(self):
        Hub.objects.bulk_create(
            Hub(
                name=self.faker.text.text(3),
                address_string=self.faker.address.address(),
                address_lat=self.faker.address.latitude(),
                address_lon=self.faker.address.longitude(),
            )
            for _ in range(100)
        )

    def _create_couriers(self):
        hubs = Hub.objects.all()
        Courier.objects.bulk_create(
            Courier(
                name=self.faker.person.full_name(),
                hub=self.faker.random.choice(hubs),
                status=self.faker.random.choice(CourierStatusChoices.names),
            )
            for _ in range(1000)
        )
