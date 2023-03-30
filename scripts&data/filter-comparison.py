#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def fn(x):
    return 1/np.sin(x)

data = np.load('filter-comparison.npy')

plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 18)
plt.plot(data[:,0], fn(data[:,0]))
plt.plot(data[:,0], data[:,1])
plt.plot(data[:,0], data[:,2])
plt.xlabel('$\phi$')
plt.ylabel('$1/\sin \phi$')
plt.legend(['Exact value', 'Approximation by $H$', "Approximation by $H'$"])
plt.savefig('../images/filter-comparison.png')
