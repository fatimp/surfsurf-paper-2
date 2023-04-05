#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def sv(x, R):
    return np.where(x < 2*R, 2*R*(np.pi - np.arccos(x/(2*R))), 2*R*np.pi)

data3 = np.loadtxt('disk-sv-3.dat')
data7 = np.loadtxt('disk-sv-7.dat')
x = np.linspace(0, 0.5, data3.size)

plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 18)
plt.plot(x, sv(x, 0.2))
plt.plot(x, data3)
plt.plot(x, data7)
plt.legend(['Theory', 'Filter $H$', "Filter $H'$"])
plt.xlabel('$r$')
plt.ylabel('$F_{sv}(r)$')
plt.savefig('../images/fsv-disk.png', bbox_inches = 'tight')
