#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

julia   = np.load("ball-sss-julia.npy")
x = np.linspace(0, julia.shape[0]/200, julia.shape[0])
x, y = np.meshgrid(x, x)
x, y, julia = x.flatten(), y.flatten(), julia.flatten()
indices = julia < 40

plt.figure(figsize = (12, 10), dpi = 300)
plt.rc('font', size = 16)
ax = plt.axes((0, 0, 1, 1,), projection = "3d")
ax.azim = -32
ax.elev =  35
ax.plot_trisurf(x[indices], y[indices], julia[indices])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel("$F_{sss}(x\mathbf{i}, y\mathbf{j})$")
ax.ticklabel_format(scilimits = (0, 0), useMathText = True)
plt.savefig('../images/ball-sss.png', bbox_inches = 'tight')
