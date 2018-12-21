# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6]])
print(a)
b = a.ravel()
print('b', b)
print(a)
c = a.flatten()
print('c', c)
print(a)
a *= 10
print('a', a, 'b', b, 'c', c)
d = a.reshape(6)
print(d)
a += 1
print(a, d, sep='\n')
