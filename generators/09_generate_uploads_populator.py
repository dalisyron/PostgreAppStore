import common.data as data
import common.random_generator as random_generator
import random
from common.builder import Builder
from random import choice

builder = Builder('\"Uploads\"', 4)

for i in range(1, 401):
    print(builder.build([i, i, random.randint(1, 5), random_generator.random_date()]))
