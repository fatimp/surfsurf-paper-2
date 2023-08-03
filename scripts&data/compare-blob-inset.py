#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp2d

data_def = np.load('ss-precise.npy')
legend = []
plt.figure(figsize = (10, 5), dpi = 300)
plt.rc('font', size = 18)
phi = np.arctan(data_def[:,1]/ data_def[:,2]) + np.pi/2

for side in [500, 1000, 2000, 3000]:
    data_julia = np.load('field-ss-%i.npy' % side)
    x = np.linspace(-1, 1, side)
    f = interp2d(x, x, data_julia)
    slice_julia = []
    for n in range(data_def.shape[0]):
        slice_julia = slice_julia + [f(data_def[n, 2], data_def[n, 1])[0]]
    slice_julia = np.array(slice_julia)
    plt.plot(phi, slice_julia, linewidth = 1.5)
    legend = legend + [str(side)]
    err = (slice_julia - data_def[:, 0])**2
    print(side, np.sqrt(sum(err)))

plt.plot(phi, data_def[:, 0], linewidth = 1.5)
plt.xlabel('$\phi$')
plt.ylabel('$F_{ss}(R, \phi)$')
plt.xlim([1.5, 3])
plt.ylim([7, 10])
#plt.legend(legend + ['Precise'])
plt.savefig('../images/fss-blob-7x7-inset.png', bbox_inches = 'tight')
