#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt('errors-3x3.dat')
data2 = np.loadtxt('errors-7x7.dat')
idx = np.arange(0, 31, 5)
c = data1[idx, 1]

plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 18)
plt.plot(idx*100 + 100, c, 'b.', markersize = 10)
plt.xlabel('Side of an image, pixels')
plt.ylabel('$C_{0.5}$')
plt.savefig('../images/c05.png', bbox_inches = 'tight')

plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 18)
plt.plot(idx*100 + 100, data1[idx, 0], 'b.', markersize = 10)
plt.plot(idx*100 + 100, data2[idx, 0], 'r.', markersize = 10)
plt.xlabel('Side of an image, pixels')
plt.ylabel('Relative error in computation of $F_{ss}$')
plt.legend(['Filter $H$', "Filter $H'$"])
plt.savefig('../images/fss-disk-errors.png', bbox_inches = 'tight')
