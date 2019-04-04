import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg
x1 = np.linspace(6, 10, 200)

M = np.array([[2., 3.], [5., 4.]])
b = np.array([4., 23.])

y1 = (4 - 2*x1)/3
y2 = (23 - 5*x1)/4

print(y1)
print(np.linalg.solve(M, b))
print(np.linalg.matrix_rank(M))
print(np.linalg.cond(M))
print(scipy.linalg.lu(M))

plt.plot(x1, y1)
plt.plot(x1, y2)
plt.show()
