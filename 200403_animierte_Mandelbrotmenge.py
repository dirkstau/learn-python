"""
Animation der iterativen Berechnung 
der Mandelbrotmenge mittels Matritzen.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

fig = plt.figure()

d, n = 200, 80  # Pixeldichte & Anzahl der Iterationen
r = 2.5  # Fluchtradius (muss größer als 2 sein)

x = np.linspace(-2.5, 1.5, 4 * d + 1)
y = np.linspace(-1.5, 1.5, 3 * d + 1)

A, B = np.meshgrid(x, y)
C = A + B * 1j

Z = np.zeros_like(C)
T = np.zeros(C.shape)

ims = []

for k in range(n):
    M = abs(Z) < r
    Z[M] = Z[M] ** 2 + C[M]
    T[M] = k + 1
    im = plt.imshow(T, cmap=plt.cm.twilight_shifted,
                    animated=True, interpolation='gaussian')
    ims.append([im])

ani = anim.ArtistAnimation(fig, ims, interval=100, blit=True, repeat_delay=0)

plt.show()
