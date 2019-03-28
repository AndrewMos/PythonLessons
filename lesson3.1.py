import numpy as np

data = np.random.rand(25)*100

data[np.argmax(data)] = 200

data[data < 50] = 0

print(data)
