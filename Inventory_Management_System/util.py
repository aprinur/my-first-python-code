import random
import string


def random_id():
    return ''.join(random.choice(string.digits + string.ascii_uppercase) for i in range(8))


