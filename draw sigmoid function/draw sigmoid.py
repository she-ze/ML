import numpy as np
import matplotlib.pyplot as plt

"""
plot the active function sigmoid
"""


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.arange(-5., 5., 0.2)
y = sigmoid(x)

# 设置图表边框以及坐标轴位置
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

plt.plot(x, y)
plt.show()

