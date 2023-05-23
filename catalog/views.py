import json

from django.shortcuts import render

from catalog.models import Product
from catalog.utils import get_model_objects, get_last_five_products


def index(request):
    data = get_model_objects(Product)
    last_five_products = get_last_five_products(data)
    context = {'data_to_display': last_five_products}
    return render(request, 'catalog/index.html', context)
