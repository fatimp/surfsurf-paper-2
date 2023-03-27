#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

data = np.load('square.npy')
data = np.where((data > 1.0) * (data < 2.3), 5*data, data)

plt.figure(figsize = (8, 8), dpi = 300)
plt.rc('font', size = 18)
plt.imshow(data, extent = (-1/2,1/2,-1/2,1/2))
plt.savefig('../images/fss-square-julia.png', bbox_inches = 'tight')
