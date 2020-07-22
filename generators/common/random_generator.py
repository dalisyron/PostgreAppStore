from random import randint
import random
import datetime

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def random_phone_number():
    return '912' + str(random_with_N_digits(7))

def get_random_date(year):
    try:
        return str(datetime.datetime.strptime('{} {}'.format(random.randint(150, 300), year), '%j %Y'))
    except ValueError:
        str(get_random_date(year))

def random_date():
    return get_random_date(2020)[:10]
