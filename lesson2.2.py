import matplotlib.pyplot as plt

filename = "files/bars.txt"
file = open(filename, "r")
tmp = []
for line in file:
    tmp.append(line)

x = [float(i) for i in tmp[0].split()]
y = [float(i) for i in tmp[1].split()]
clr = [float(i) for i in y]
print(x, y)
for cx, cy, c in zip(x, y, clr):
    plt.bar(cx, cy, 0.5, color=[c, 0, 0, 0.5])
plt.show()
