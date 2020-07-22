import common.data as data
import common.random_generator as random_generator
import random
from common.builder import Builder
from random import choice

builder = Builder('\"Apps\"', 4)

for i in range(101, 401):
    print(builder.build([i - 100, 'The ' + choice(data.usernames) + ' App', random.randint(1, 17), i]))
