#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('../../../utils/clases.mplstyle')
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

t = np.linspace(0, 200, 100)
xp = 25 * t - 0.5 * 0.1 * t**2
xc = 200 + 15 * t

ax = plt.gca()
ax.plot(t, xp, label='tren de pasajeros')
ax.plot(t, xc, label='tren de cargas')
# ax.xaxis.set_major_locator(MultipleLocator(1))
# ax.xaxis.set_minor_locator(MultipleLocator(1/6))
plt.xlabel(r'$t$ [s]')
plt.ylabel(r'$x$ [m]')

plt.grid(which='both', ls='-')
plt.legend()
plt.tight_layout()
plt.savefig("ac-13.pdf")
