# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import datetime as dt

n = 100000
# 基于python的实现
start = dt.datetime.now()
A, B = [], []
for i in range(n):
    A.append(i ** 2)
    B.append(i ** 3)

C = []

for a, b in zip(A, B):
    C.append(a + b)


print((dt.datetime.now() - start).microseconds)

# 基于numpy的实现

start = dt.datetime.now()
A, B = np.arange(n) ** 2, np.arange(n) ** 3
C = A + B

print((dt.datetime.now() - start).microseconds)
