import matplotlib.pyplot as plt
import numpy as np

dataX = np.load('files/daneX.npy')
dataY = np.load('files/daneY.npy')

H, xedges, yedges = np.histogram2d(dataX, dataY, bins=100)

cmap = plt.get_cmap('PiYG') #etomeniat'

plt.pcolormesh(H, cmap=cmap)
plt.colorbar()
plt.show()
