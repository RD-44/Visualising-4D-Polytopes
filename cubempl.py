import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import itertools as iter
import numpy as np
from math import sin, cos

fig3d = plt.subplot(121, projection='3d')
fig2d = plt.subplot(122)
plt.subplots_adjust(bottom=0.25)

def rotate(point, a, b): # Applies 3D rotation matrix
    x, y, z = point
    c1, s1, c2, s2 = cos(a), sin(a), cos(b), sin(b)
    return (c2*x + s2*z, s1*s2*x + c1*y - s1*c2*z, s1*y + c1*c2*z - s2*c1*x)

def update(h, a, b):
    fig2d.clear()
    fig3d.clear()
    points = iter.product([-1, 1], repeat=3)
    for p in points:
        x, y, z = p  
        rx, ry, rz = rotate(p, a, b)
        dest = [rotate((-x, y, z), a, b), rotate((x, -y, z), a, b), rotate((x, y, -z), a, b)]
        sf = np.divide(h, h-rz)  
        # Connecting vertex to the 3 neighbouring vertices
        for d in dest:
            dx, dy, dz = d
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