import scipy.optimize as opt
import numpy as np


def f(xy):
    x, y = xy
    return 0.5 + (np.sin(x ** 2 - y ** 2) ** 2 - 0.5) / (1 + 0.001 * (x ** 2 + y ** 2)) ** 2


pocz = np.random.randn(2)
minimum = opt.fmin(f, pocz)
# minimum = opt.fmin(f, (0, 0))

print(minimum)
xy = (minimum[0], minimum[1])
print(f(xy))
