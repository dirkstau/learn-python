"""Visualisierung der Zahl pi auf 1 Mio Nachkommastellen."""

import turtle as tu

LINES = 1_000_000

tu.mode('logo')
tu.tracer(False)
tu.screensize(3000, 3000, 'black')
tu.pencolor('red')
tu.colormode(255)

with open("pi1000000.txt", "r") as f:
    pi = f.read()

for n in range(LINES):
    zahl = int(pi[n])
    color = int(n/(LINES/255))
    tu.pencolor(255-color, color, 255-color)
    rotation = zahl * 36
    tu.setheading(rotation)
    tu.forward(2)
    if n % 10_000 == 0:
        tu.update()

tu.done()
