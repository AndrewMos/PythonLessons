import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg
x1 = np.linspace(-10, 10, 200)

M = np.array([[2., 3., 0.], [5., 4., 0.], [0., 5., 0.]])
b = np.array([4., 23., 18.])

y1 = (4 - 2*x1)/3
y2 = (23 - 5*x1)/4
y3 = (18 - 0*x1)/5
a = np.linalg.lstsq(M, b, rcond=-1)
print(a)

plt.scatter(a[0][0], a[0][1])
plt.plot(x1, y1)
plt.plot(x1, y2)
plt.plot(x1, y3)
plt.plot()
plt.show()
