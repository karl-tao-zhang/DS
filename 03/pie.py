# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp

values = [26, 17, 21, 11, 25]
spaces = [0.05, 0.01, 0.01, 0.01, 0.02]
labels = ['Python', 'JavaScript', 'C++', 'C', 'Java']
colors = ['dodgerblue', 'orangered', 'limegreen', 'violet', 'gold']

mp.figure('Pie', facecolor='lightgray')
mp.title('Pie', fontsize=20)
mp.pie(values, spaces, labels, colors, '%d%%', shadow=True, startangle=90)

mp.axis('equal')

mp.show()
