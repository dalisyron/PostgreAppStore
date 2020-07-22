#id
#package_name
#dev_id
#size
#file

import common.data as data
import common.random_generator as random_generator
import random
from common.builder import Builder
from random import choice

builder = Builder('\"Packages\"', 5)

for i in range(1, 401):
    print(builder.build([i, 'com.' + choice(data.usernames) + '.pac', random.randint(1, 5), random.randint(1, 10000), 'file.apk']))
