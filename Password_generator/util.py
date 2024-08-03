import random
import string


def random_pass(panjang: int):
    result = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(panjang))
    return result


