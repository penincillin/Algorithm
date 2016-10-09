import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# curve fitting
x = np.arange(0, 10)
y = np.exp(-x/3.0)
f1 = interp1d(x, y)
for i in xrange(0, 9):
    x_i = i+0.5
    print x_i, f1(x_i), np.exp(-x_i/3.0)

# find intersection point of two curves
f2 = lambda x: 1-x
f = lambda x: f1(x)-1+x
print fsolve(f, 0.0)
