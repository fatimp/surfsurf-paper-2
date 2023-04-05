#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def sv(x, R):
    return np.where(x < 2*R, np.pi*R*x + 2*np.pi*R**2, 4*np.pi*R**2)

data3 = np.loadtxt('ball-sv-3.dat')
data7 = np.loadtxt('ball-sv-7.dat')
x = np.linspace(0, 0.5, data3.size)

plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 18)
plt.plot(x, sv(x, 0.2))
plt.plot(x, data3)
plt.plot(x, data7)
plt.legend(['Theory', 'Filter $H$', "Filter $H'$"])
plt.xlabel('$r$')
plt.ylabel('$F_{sv}(r)$')
plt.savefig('../images/fsv-ball.png', bbox_inches = 'tight')
