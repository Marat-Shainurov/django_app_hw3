import json

from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()

        with open('data_product.json', encoding='utf-8') as file:
            data = json.load(file)

        products_to_add = []
        for prod in data:
            products_to_add.append(Product(
                id=prod['pk'], name=prod['fields']['name'], description=prod['fields']['description'],
                img=prod['fields']['img'], category=prod['fields']['category'],
                price=prod['fields']['price'], creation_date=prod['fields']['creation_date'],
                last_change_date=prod['fields']['last_change_date'])
            )

        Product.objects.bulk_create(products_to_add)
