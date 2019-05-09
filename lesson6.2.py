import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# columns: 1. petal length, 2. sepal length, 3. sepal width


data = np.loadtxt('files/PCAdata.txt')
covmat = np.cov(data)
print(covmat)

m = [np.mean(data[0]), np.mean(data[1]), np.mean(data[2])]
print(m)

w, v = np.linalg.eig(covmat)

print(w, v)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(data[0], data[1], data[2], '.')

plt.show()
