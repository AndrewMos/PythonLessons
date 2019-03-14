import matplotlib.pyplot as plt

filename = "files/pie.txt"
file = open(filename, "r")

x = [float(i) for i in file.readline().split()]

plt.pie(x, explode=[0.2, 0.03, 0.03, 0.03, 0.03])
plt.show()
