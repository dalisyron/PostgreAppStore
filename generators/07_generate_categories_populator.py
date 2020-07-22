import common.data as data
import common.random_generator as random_generator
import random
from common.builder import Builder
from random import choice

builder = Builder('\"Categories\"', 2)

genres = ["Productivity",
"Email",
"Maps",
"Tools",
"Video Player",
"Music",
"Social",
"Educational",
"Shop",
"Travel",
"Entertainment",
"Children",
"Sports",
"Weather",
"Fitness",
"Cooking",
"Health"]

for i in range(1, 18):
    print(builder.build([i, genres[i - 1]]))
