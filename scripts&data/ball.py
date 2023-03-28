#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

data3 = np.loadtxt('ball-3x3.dat')
data5 = np.loadtxt('ball-5x5.dat')

def ss(x, R):
    return np.where(x < 2*R, 2*np.pi*R**2/x, 0)

def sv(x, R):
    return np.where(x < 2*R, np.pi*R*x + 2*np.pi*R**2, 4*np.pi*R**2)


R = 0.24

x = np.linspace(0.01, 0.5, 1000)
th = ss(x, R)
d3i = interp1d(np.linspace(0, 0.5, data3.size), data3 * 450**2)
d3s = d3i(x)
print(np.sum((d3s - th)**2) / np.sum(th**2))
d5i = interp1d(np.linspace(0, 0.5, data5.size), data5 * 450**2)
d5s = d5i(x)
print(np.sum((d5s - th)**2) / np.sum(th**2))

plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 18)

x = np.linspace(0, 0.5, 1000)
plt.plot(np.linspace(0, 0.5, data3.size), data3 * 450**2, 'b', linewidth = 1.2)
plt.plot(np.linspace(0, 0.5, data5.size), data5 * 450**2, 'g', linewidth = 1.2)
plt.plot(x, ss(x, R), 'r', linewidth = 1.2)
plt.ylim([0, 10])
plt.xlim([0.03, 0.5])
plt.xlabel('$r$')
plt.ylabel('$F_{ss}(r)$')
plt.legend(['Filter 3x3', 'Filter 5x5', 'Therory'])
plt.savefig('../images/ball-3d-ss.png')
