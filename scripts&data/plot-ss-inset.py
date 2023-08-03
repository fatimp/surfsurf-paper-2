#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

def ss(x, R):
    return np.where(x < 2*R, 4*R**2/(x * np.sqrt(4*R**2 - x**2)), 0)

legend = []
plt.figure(figsize = (10, 5), dpi = 300)
plt.rc('font', size = 18)

for side in [100, 500, 1000, 2000, 3000]:
    data = np.loadtxt('disks-%i-we-ss.dat' % side)
    plt.plot(np.linspace(0, 0.5, data.size), data * side**2, linewidth = 1.8)
    legend = legend + [str(side)]

xs = np.linspace(0, 0.5, 1000)
plt.xlim([0.03, 0.06])
plt.ylim([2.0, 2.4])
plt.plot(xs, ss(xs, 0.0334), linewidth = 1.8)
plt.ticklabel_format(axis = "x", scilimits = (0, 0), useMathText = True)
#plt.legend(legend + ['Theory'])
plt.xlabel('Correlation length $r$')
plt.ylabel('$F_{ss}(r)$')
plt.savefig('../images/fss-disk-7x7-inset.png', bbox_inches = 'tight')
