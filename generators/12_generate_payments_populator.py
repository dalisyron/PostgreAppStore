import common.data as data
import common.random_generator as random_generator
import random
from common.builder import Builder
from random import choice

builder = Builder('\"Payments\"', 6)

for i in range(1, 1000):
    d1 = random_generator.random_date()
    d2 = random_generator.random_date()
    print(builder.build([i, random.randint(1, 500), random.randint(1, 5) * 1000, choice(['SUCCESS', 'FAILURE']), min(d1, d2), max(d1, d2)]))
