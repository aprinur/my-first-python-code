import random
import string


def order_id():
    _id = ''.join(random.choice(string.digits + string.ascii_letters) for i in range(8))
    return _id


def random_table_number():
    number = random.choice(range(1, 12))
    return number






