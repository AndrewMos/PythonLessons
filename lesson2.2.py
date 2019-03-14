import matplotlib.pyplot as plt

filename = "files/bars.txt"
file = open(filename, "r")
tmp = []
for line in file:
    tmp.append(line)

x = [float(i) for i in tmp[0].split()]
y = [float(i) for i in tmp[1].split()]

for cx, cy in zip(x, y):
    plt.bar(cx, cy, 0.5, color=[cy, 0, cy, 1])
plt.show()
