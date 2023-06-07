import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import itertools as iter
import numpy as np
from math import sin, cos

# This is an example to show projection of 3d cube into 2d plane
fig3d = plt.subplot(121, projection='3d')
fig2d = plt.subplot(122)
plt.subplots_adjust(bottom=0.25)

points = list(iter.product([-1, 1], repeat=3))

def distsquared(p1, p2): return sum((p1[i]-p2[i])**2 for i in range (3))

neighbours = {}
for p in points:
    neighbours[p] = set()
    for k in points:
        if distsquared(p, k) == 4 and not (k in neighbours and p in neighbours[k]):
            neighbours[p].add(k)

def rotate(point, a, b): # Applies 3D rotation matrix
    x, y, z = point
    c1, s1, c2, s2 = cos(a), sin(a), cos(b), sin(b)
    return (c2*x + s2*z, s1*s2*x + c1*y - s1*c2*z, s1*y + c1*c2*z - s2*c1*x)

def update(h, a, b):
    fig2d.clear()
    fig3d.clear()
    
    for p in points:
        rx, ry, rz = rotate(p, a, b)
        sf = np.divide(h, h-rz)  

        for d in neighbours[p]:
            dx, dy, dz = rotate(d, a, b)
            dsf = np.divide(h, h-dz)
            fig2d.plot([sf*rx, dsf*dx], [sf*ry, dsf*dy], c="red")
            fig3d.plot([rx, dx], [ry, dy], [rz, dz], c="red")

h_slider = Slider(
    ax=plt.axes([0.2, 0.05, 0.65, 0.03]),
    label="h",
    valmin=-10,
    valmax=10,
    valinit=5,
    valstep=0.1,
)
h_slider.on_changed(lambda x : update(x, a_slider.val, b_slider.val))

a_slider = Slider(
    ax=plt.axes([0.2, 0.15, 0.65, 0.03]),
    label="Angle about y axis",
    valmin=-5,
    valmax=5,
    valinit=0,
    valstep=0.1,
)
a_slider.on_changed(lambda x : update(h_slider.val, x, b_slider.val))

b_slider = Slider(
    ax=plt.axes([0.2, 0.25, 0.65, 0.03]),
    label="Angle about x axis",
    valmin=-5,
    valmax=5,
    valinit=0,
    valstep=0.1,
)
b_slider.on_changed(lambda x : update(h_slider.val, a_slider.val, x))

update(5, 0, 0)
plt.show()