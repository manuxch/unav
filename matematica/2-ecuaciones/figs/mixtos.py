#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('../../../utils/clases.mplstyle')
from math import sqrt

def f1(x):
    return x**2 - 2*x -3

def f2(x):
    return 1-2*x

x = np.linspace(-5, 5, 100)
plt.plot(x, f1(x))
plt.plot(x, f2(x))
plt.plot([-2, 2],[5, -3], 'o')
plt.axhline(y=0, c='k', alpha=0.4)
plt.axvline(x=0, c='k', alpha=0.4)
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.tight_layout()
plt.savefig('mixtos.pdf')
