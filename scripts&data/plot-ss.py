#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

def ss(x, R):
    return np.where(x < 2*R, 4*R**2/(x * np.sqrt(4*R**2 - x**2)), 0)

legend = []
plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 18)

for side in range(100, 3200, 500):
    data = np.loadtxt('disks-%i-we-ss.dat' % side)
    plt.plot(np.linspace(0, 0.5, data.size), data * side**2, linewidth = (side == 3100 and 1.2 or 0.5))
    legend = legend + [str(side)]

xs = np.linspace(0, 0.5, 1000)
plt.xlim([0, 0.1])
plt.ylim([0, 4])
plt.plot(xs, ss(xs, 0.0334), linewidth = 1.2)
plt.ticklabel_format(axis = "x", scilimits = (0, 0), useMathText = True)
plt.legend(legend + ['Theory'])
plt.xlabel('Correlation length $r$')
plt.ylabel('$F_{ss}(r)$')
plt.savefig('../images/fss-disk-3x3.png')
