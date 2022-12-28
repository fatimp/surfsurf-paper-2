#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('angles-5x5.dat')

plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 18)

plt.plot(data[:,0], data[:,1])
plt.plot(data[:,0], 1/np.sin(data[:,0]))
plt.legend(["Approximation with filter $H'$", 'Exact'])
plt.xlabel('$\phi$')
plt.ylabel('$1/\sin \phi$')
plt.savefig('../images/angles-5x5.png')
