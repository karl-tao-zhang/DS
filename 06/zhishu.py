# -*- coding: utf-8 -*-
from __future__ import unicode_literals

l = []

for i in range(2, 100):
    for j in l:
        if j**2 > i:
            l.append(i)
            break
        if i % j == 0:
            break
    else:
        l.append(i)

print(l)
