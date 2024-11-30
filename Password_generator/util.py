import random
import string


def random_pass(panjang: int):
    result = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(panjang))
    if len(result) == panjang:
        return result


def random_passw():
    while True:
        x = 1
        access = '65g4a6g4a6'
        password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(x))

        if password == access:
            break
        else:
            x += 1
            continue


print(random_pass(8))