import numpy as np
from scipy.misc import toimage

from numpy_turtle import Turtle, l_system



"""Create a fractal plant"""
axiom = 'X'
rules = {
    'X': 'F+[[X]-X]-F[-FX]+X',
    'F': 'FF',
}

angle = np.pi / 7
cols, rows = 512, 512
padding = 32
n = 6

a = np.zeros((rows, cols))
s = l_system.grow(axiom, rules, n)

t = Turtle(a)
t.position = rows - padding, padding
t.rotate(np.pi - angle)

for s_n in s:
    if s_n == 'F':
        t.forward(3)
    elif s_n == '-':
        t.rotate(-angle)
    elif s_n == '+':
        t.rotate(angle)
    elif s_n == '[':
        t.push()
    elif s_n == ']':
        t.pop()

toimage(a).show()
