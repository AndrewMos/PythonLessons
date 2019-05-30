import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

dt = np.load('files/rozklady.npz')
arr = np.linspace(-6, 6, num=100)

data = []
data.append(dt['arr_0'])
data.append(dt['arr_1'])
data.append(dt['arr_2'])

fig, ax = plt.subplots(nrows=1, ncols=3)

f1 = stats.gaussian_kde( data[0][0] )
f2 = stats.gaussian_kde( data[0][1] )

ax[0].plot(f1(arr))
ax[0].plot(f2(arr))

f1 = stats.gaussian_kde( data[1][0] )
f2 = stats.gaussian_kde( data[1][1] )

ax[1].plot(f1(arr))
ax[1].plot(f2(arr))

f1 = stats.gaussian_kde( data[2][0] )
f2 = stats.gaussian_kde( data[2][1] )

ax[2].plot(f1(arr))
ax[2].plot(f2(arr))



plt.show()
