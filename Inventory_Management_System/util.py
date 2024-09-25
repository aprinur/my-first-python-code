import random
import string


def random_id():
    return ''.join(random.choice(string.digits + string.ascii_uppercase)
                   for i in range(8))


def find_key_by_value(nested_dict, target):
    for key, value in nested_dict.items():
        if value.get('name') == target:
            return key

    return None

