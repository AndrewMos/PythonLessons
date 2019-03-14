import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import interp

filename = "files/scatter.txt"
file = open(filename, "r")
tmp = []
x = []
y = []

for line in file:
    tmp.append(line)

for word in tmp[0].split():
    x.append(float(word))

for word in tmp[1].split():
    y.append(float(word))
file.close

plt.axes(polar=True)

data = []
for num in y:
    data.append((num+5)*20)

clr = cm.copper(data)

plt.scatter(x, y, 10, y)
plt.show()



# filename = "files/data2.dat"
# file = open(filename, "r")
# for str in file.read():
#     y.append(str)
#
# plt.plot(x, y)
# plt.show()
