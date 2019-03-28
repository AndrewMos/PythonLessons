import numpy as np
import matplotlib.pyplot as plt

data = (np.random.rand(1000)-0.5)*2
# data = data.reshape(500, 2)
print(data)

t = np.sqrt(data[::2]**2 + data[1::2]**2)
print(t)
r = np.arctan2(data[1::2], data[::2])


plt.axes(polar=True)

plt.scatter(r, t, 2)
plt.show()
