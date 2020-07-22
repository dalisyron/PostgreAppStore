import common.data as data
import common.random_generator as random_generator
import random
from common.builder import Builder
from random import choice

builder = Builder('\"Genres\"', 2)

genres = ["Action-Adventure",
"Metroidvania",
"Stealth-Based Game",
"Survival Sandbox",
"Survival Horror",
"Platform Game",
"Cinematic Platform Game",
"Elimination Platformer",
"Puzzle Platformer",
"Run-and-Gun",
"Beat em Up",
"Hack and Slash",
"Stylish Action",
"Fighting Game",
"Mascot Fighter",
"Platform Fighter",
"FPS",
"Hero Shooter"]

for i in range(1, 19):
    print(builder.build([i, genres[i - 1]]))
