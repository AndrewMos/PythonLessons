import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

data1 = np.random.normal(0.0, 1.0, 100)
data2 = np.random.normal(2.0, 0.8, 100)
arr = np.linspace(-5, 5, num=200)

f = stats.gaussian_kde( np.hstack([data1, data2]) )

plt.hist(np.hstack([data1, data2]), normed=1)
plt.plot(arr,  f(arr) )

plt.show()
