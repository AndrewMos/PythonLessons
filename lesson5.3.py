import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

data = np.load('files/inter1D.npz')
dataX = data['x']
dataY = data['y']

r = np.linspace(-1, 1, 12)
plt.plot(r, np.interp(r, dataX, dataY), '--o')

f = interpolate.interp1d(dataX, dataY, kind='cubic')

g = np.linspace(-1, 1, 100)
new = f(g)

plt.plot(g, new, '-', color='red')

plt.show()
