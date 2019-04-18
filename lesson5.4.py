import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


data = np.load('files/inter2D.npz')
dataX = data['x']
dataY = data['y']
dataZ = data['z']

X, Y = np.meshgrid(dataX, dataY)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_wireframe(X, Y, dataZ)

plt.show()
