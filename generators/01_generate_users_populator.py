#id
#username
#first_name
#last_name
#email
#phone_number
import common.data as data
import common.random_generator as random_generator
from common.builder import Builder
from random import choice

builder = Builder('\"Users\"', 6)

for i in range(1, 6):
    print(builder.build([i, choice(data.usernames), choice(data.first_names), choice(data.last_names), choice(data.emails), random_generator.random_phone_number()]))
