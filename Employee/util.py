import string
import random


def ran(length):
    result = ''.join(random.choice(string.digits)for i in range(length))
    return result