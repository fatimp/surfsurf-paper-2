#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as inter

julia   = np.load("ball-sss-julia.npy")
precise = np.load("ball-sss-precise.npy")

julia_x = np.linspace(0, julia.shape[0]/200, julia.shape[0])
f = inter.RegularGridInterpolator((julia_x, julia_x),  julia)
x = np.linspace(0.02, 0.61, precise.shape[0])
x, y = np.meshgrid(x, x)
julia = f(np.stack((x, y), axis = 2))

error = np.abs(precise - julia)
error = error / np.clip(precise, 1e-8, 1e8)

x, y, error = x.flatten(), y.flatten(), error.flatten()
indices = (x**2 + y**2) < 0.575**2

plt.figure(figsize = (12, 10), dpi = 300)
plt.rc('font', size = 16)
ax = plt.axes((0, 0, 1, 1,), projection = "3d")
ax.azim = -32
ax.elev =  35
ax.plot_trisurf(x[indices], y[indices], error[indices])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Relative error')
ax.ticklabel_format(scilimits = (0, 0))
plt.savefig('../images/ball-sss-error.png', bbox_inches = 'tight')
