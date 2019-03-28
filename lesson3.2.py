import numpy as np

data = (np.random.randint(-100, 100, size=(9, 9)))

ans = np.sort(data[data % 2 == 0])

print(ans)
