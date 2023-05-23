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
            products_to_add.append(Product(**prod))

        Product.objects.bulk_create(products_to_add)