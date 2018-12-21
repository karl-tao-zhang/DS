# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np

a = np.arange(11, 20).reshape(3, 3)
print('a')
print(a)
b = np.arange(21, 30).reshape(3, 3)
print('b')
print(b)
c = np.arange(31, 40).reshape(3, 3)
print('c')
print(c)

d = np.vstack((a, b, c))
print('d')
print(d)

e = np.concatenate((a, b, c), axis=1)
print('e')
print(e)
f, g, h = np.vsplit(e, 3)
print('f,g,h')
print(f, g, h, sep='\n')

i = np.hstack((a, b, c))
print('i')
print(i)
j = np.concatenate((a, b, c), axis=1)
print('j')
print(j)

k, l, m = np.hsplit(j, 3)
print('k,l,m')
print(k, l, m, sep='\n')

n = np.dstack((a, b))
print('n')
print(n)

o, p = np.dsplit(n, 2)
print('o,p')
print('o', o, 'p', p, sep='\n')
print(o.T)
