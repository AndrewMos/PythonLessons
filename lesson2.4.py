import matplotlib.pyplot as plt

filename = "files/data2.dat"
file = open(filename, "r")

x = [float(line) for line in file]
print(x)

plt.subplot(122)
plt.hist(x, density=1, histtype='step', cumulative=True)
plt.subplot(121)
plt.hist(x, histtype='step')

plt.show()
