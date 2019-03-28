import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3*np.pi, 0.01)

plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

plt.scatter(x[np.abs(np.sin(x)-np.cos(x)) < 0.1], np.sin(x[np.abs(np.sin(x)-np.cos(x)) < 0.1]))
plt.scatter(x[np.abs(np.sin(x)-np.cos(x)) < 0.1], np.cos(x[np.abs(np.sin(x)-np.cos(x)) < 0.1]))

plt.show()
