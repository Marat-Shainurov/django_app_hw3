def get_model_objects(model) -> list:
    """Takes a model name. Returns the list of the model's objects"""
    data = model.objects.all()
    list_data = list(data.values())
    return list_data


def get_last_five_products(products_list: list) -> list:
    """Takes a list of a model's list. Returns the list of last 5 objects"""
    sorted_products_list = sorted(products_list, key=lambda x: x['id'])
    return sorted_products_list[-5:]
