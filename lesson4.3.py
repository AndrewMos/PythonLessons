import numpy as np
import matplotlib.pyplot as plt
x1 = np.linspace(0.9, 1.1, 200)

y1 = []
for x in x1:
    y1.append(np.linalg.cond([[1., np.sqrt(x)], [1., 1./np.sqrt(x)]]))


plt.plot(x1, y1)
plt.show()
