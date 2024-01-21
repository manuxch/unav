#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('../../../utils/clases.mplstyle')
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

t = np.array([0, 2.1, 20, 53])
v = np.array([0, 96, 320, 405])

ax = plt.gca()
ax.plot(t, v, 'o')
# ax.xaxis.set_major_locator(MultipleLocator(1))
# ax.xaxis.set_minor_locator(MultipleLocator(1/6))
plt.xlabel(r'$t$ [s]')
plt.ylabel(r'$|v|$ [km/h]')

plt.grid(which='both', ls='-')
plt.tight_layout()
plt.savefig("ac-08.pdf")
