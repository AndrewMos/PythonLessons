import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

dataX = np.load('files/daneX.npy')
dataY = np.load('files/daneY.npy')

H, xedges, yedges = np.histogram2d(dataX, dataY, bins=200)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(0, 200, 1)
X, Y = np.meshgrid(x, y)

ax.plot_surface(X, Y, H, cmap='jet')

plt.show()
