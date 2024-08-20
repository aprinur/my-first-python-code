import time
from datetime import datetime


def close():
    print('program will be exit in')
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('Program closed')
    time.sleep(1)
    exit()


template = {
    'task': 'xxxx',
    'place': 'xxxx',
    'date': 'dd-mm-yyyy'

}


def is_valid_date(year, month, day):
    try:
        date = datetime(year, month, day)
        return True
    except ValueError:
        return False