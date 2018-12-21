# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# import numpy as np
import random

poison_bottle = random.randint(1, 1000)

mouses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# mdir = {}
dead_mouse = []
for mouse in mouses:
    for i in range(1, 1001):
        if bin(i)[mouse - 1] == 1:
            dead_mouse.append(i)


find_bottle = bin(0)

for a in dead_mouse:
    find_bottle[a - 1] == 1
find_bottle = dec(find_bottle)
print(find_bottle)
# mdir += {'mouse': []}


# {1: [], 2: [], ...}

# dead_mouse = []

# ...poison_bottle

# dead_mouse = [5, 4, 1]

# ...dead_mouse
# find_bottle = 25?

# print(poison_bottle)
# print(find_bottle)
