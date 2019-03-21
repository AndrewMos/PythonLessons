import matplotlib.pyplot as plt

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                str(height),
                ha='center', va='bottom')

filename = "files/bars.txt"
file = open(filename, "r")
tmp = []
for line in file:
    tmp.append(line)

x = [float(i) for i in tmp[0].split()]
y = [float(i) for i in tmp[1].split()]

for cx, cy in zip(x, y):
    rect = plt.bar(cx, cy, 0.5, color=[cy, 0, cy, 1])
    autolabel(rect)

plt.show()
