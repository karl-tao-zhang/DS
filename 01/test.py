# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# 列表推导式求出100以内质数
[x for x in range(2, 101) if [y for y in range(2, x) if x %
                              y != 0]]  # 不充分但是必要的条件


[x for x in range(2, 101) if not [y for y in range(2, x) if x % y == 0]]
