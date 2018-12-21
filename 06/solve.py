# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np

A = np.mat('1 -2 1;0 22 -8; -4 5 9')
B = np.mat('0;8;-9')
x = np.linalg.solve(A, B)
print(x)
print(np.linalg.lstsq(A, B))
