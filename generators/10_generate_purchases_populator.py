import common.data as data
import common.random_generator as random_generator
import random
from common.builder import Builder
from random import choice

builder = Builder('\"Purchases\"', 6)

for i in range(1, 501):
    print(builder.build([i, random.randint(1, 400), random.randint(1, 5), choice([0, 1]), '12hj$#@323xs21', '23ZZAsW']))
