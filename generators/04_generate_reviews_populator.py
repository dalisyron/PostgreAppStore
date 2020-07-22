import common.data as data
import common.random_generator as random_generator
import random
from common.builder import Builder
from random import choice

builder = Builder('\"Reviews\"', 6)

for i in range(1, 401):
    print(builder.build([i, random_generator.random_date(), 'This is a review', random.randint(1, 5), random.randint(1, 20), random.randint(1, 5)]))
