import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy import interpolate

data = np.load('files/inter2D.npz')
dataX = data['x']
dataY = data['y']
dataZ = data['z']


f = interpolate.interp2d(dataX, dataY, dataZ, kind='cubic')
newX = np.linspace(0, 10, 50)
newY = np.linspace(0, 10, 50)
newZ = f(newX, newY)
newX, newY = np.meshgrid(newX, newY)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(newX, newY, newZ, cmap='jet')

plt.show()
