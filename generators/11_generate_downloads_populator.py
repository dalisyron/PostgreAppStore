import common.data as data
import common.random_generator as random_generator
import random
from common.builder import Builder
from random import choice

builder = Builder('\"Downloads\"', 4)

for i in range(1, 1000):
    print(builder.build([i, random.randint(1, 400), random.randint(1, 5), random_generator.random_date()]))
