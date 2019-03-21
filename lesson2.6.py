import matplotlib.pyplot as plt

x, y = [0, 10, 20, 30, 40], [0, 23, 27, 29, 30]

plt.plot(x, y, linestyle='-.', marker='o', color='red', linewidth=3, markersize=8, markerfacecolor='blue')

plt.tick_params(labelbottom=False)
plt.tick_params(labelleft=False)


plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color=(0, 0, 0, 1))
plt.grid(which='minor', linestyle=':', linewidth='0.5', color=(0, 0, 0, 0.1))

plt.show()
