#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('../../../utils/clases.mplstyle')
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

t, d = np.loadtxt("bruno2.dat", unpack=True)

ax = plt.gca()
ax.plot(t, d, '-')
ax.xaxis.set_major_locator(MultipleLocator(50))
# ax.xaxis.set_minor_locator(MultipleLocator(1/6))
plt.xlabel(r'Tiempo [s]')
plt.ylabel(r'$v$ [km/h]')

plt.grid(which='both', ls='-')
plt.tight_layout()
plt.savefig("bruno-2.pdf")
