# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp


def wave(N):
    k = np.arange(1, N + 1)

    def f(x):
        return 4 / np.pi * np.sum(np.sin((2 * k - 1) * x) / (2 * k - 1))
    return np.frompyfunc(f, 1, 1)
x = np.linspace(0, 2 * np.pi, 200)
y1 = wave(1)(x)
y2 = wave(2)(x)
y3 = wave(3)(x)
y4 = wave(10)(x)
y5 = wave(100)(x)
y6 = wave(1000)(x)
mp.figure('wave', facecolor='lightgray')
mp.title('wave', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x, y1, label='N=1')
mp.plot(x, y2, label='N=2')
mp.plot(x, y3, label='N=3')
mp.plot(x, y4, label='N=10')
mp.plot(x, y5, label='N=100')
mp.plot(x, y6, label='N=1000')
mp.legend()
mp.show()
