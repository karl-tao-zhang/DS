# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
# 得到x
x = np.linspace(-np.pi, np.pi, 1000)
# 得到函数
cos_y = np.cos(x) / 2
sin_y = np.sin(x)
# 得到特殊点
xo = np.pi * 3 / 4
yo_cos = np.cos(xo) / 2
yo_sin = np.sin(xo)
# x,y扩大
mp.xlim(x.min() * 1.1, x.max() * 1.1)
mp.ylim(sin_y.min() * 1.1, sin_y.max() * 1.1)
# 得到十字叉
mp.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2,
           np.pi * 3 / 4, np.pi],
          [r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$',
           r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$',
           r'$\pi$'])
mp.yticks([-1, -0.5, 0.5, 1])
# 获得当前轴
ax = mp.gca()
# 对坐标轴进行移动和隐藏
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# plot就是连接直线  如果点太多就会形成曲线
mp.plot(x, cos_y, linestyle='-', linewidth=2,
        color='dodgerblue',
        label=r'$y=\frac{1}{2}cos(x)$')
mp.plot(x, sin_y, linestyle='-', linewidth=2,
        color='orangered', label=r'$y=sin(x)$')
# 连接的虚线
mp.plot([xo, xo], [yo_cos, yo_sin], linestyle='--',
        linewidth=1, color='limegreen')
# s是大小 edgecolor边缘色 facecolor填充色，zorder指z方向上的顺序，就是垂直于屏幕的顺序
mp.scatter([xo, xo], [yo_cos, yo_sin], s=60,
           edgecolor='limegreen',
           facecolor='white', zorder=3)
# 显示图例
mp.legend()
# 得到图 运行
mp.show()
