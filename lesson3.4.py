import numpy as np
import matplotlib.pyplot as plt

data = (np.random.rand(1000)-0.5)*2

t = np.sqrt(data[::2]**2 + data[1::2]**2)
r = np.arctan2(data[1::2], data[::2])

plt.axes(polar=True)


plt.scatter(r, t, 4, cmap =plt.cm.terrain, c=r)#(r+np.pi)/(2*np.pi))
plt.show()
