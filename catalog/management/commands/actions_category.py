import json

from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()

        with open('data_category.json', encoding='utf-8') as file:
            data = json.load(file)

        category_to_add = []
        for category in data:
            category_to_add.append(
                Category(id=category['pk'], category_name=category['fields']['category_name'],
                         category_description=category['fields']['category_description']))

        Category.objects.bulk_create(category_to_add)
