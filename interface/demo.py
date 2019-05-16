# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

# Prepare arrays x, y, z
theta = np.linspace(-4 * np.pi, 4 * np.pi,99)
a = 1
r= 5
x = a + (r-a) * np.cos(theta)
y = (r-a) * np.sin(theta)
z = 2*(a*(r-a))** (1/2) * np.sin(theta/2)
ax.plot(x, y, z, label='parametric curve')

ax.legend()

plt.show()