import matplotlib.pyplot as plt
import numpy as np


data = np.loadtxt('files/populacje.txt').tolist()

years = np.asarray([i[0] for i in data])
hares = np.asarray([i[1] for i in data])
foxes = np.asarray([i[2] for i in data])
carot = np.asarray([i[3] for i in data])


print('mean hares :' + str(hares.mean()))
print('mean foxes :' + str(foxes.mean()))
print('mean carots :' + str(carot.mean()))

print('std hares :' + str(hares.std()))
print('std foxes :' + str(foxes.mean()))
print('std carots :' + str(carot.mean()))

maxh = years[hares == hares.max()]
maxf = years[foxes == foxes.max()]
maxc = years[carot == carot.max()]

print(maxh, maxf, maxc)

maxh = years[hares > 50000]
maxf = years[foxes > 50000]
maxc = years[carot > 50000]

print(maxh, maxf, maxc)

diff = np.gradient(hares)

print(np.corrcoef(foxes, diff))

plt.plot(years, hares, color='blue')
plt.plot(years, foxes, color='red')
# plt.plot(years, carot, color='yellow')
plt.plot(years, diff, '--')

plt.show()
