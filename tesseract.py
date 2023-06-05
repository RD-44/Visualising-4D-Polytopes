import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import itertools as iter
import numpy as np
from math import sin, cos

fig = plt.subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.25)

def rotate(point, a, b): # Applies 4D rotation matrix
    x, y, z, w = point
    c1, s1, c2, s2 = cos(a), sin(a), cos(b), sin(b)
    return (c1*x - s1*y, s1*x + c1*y, c2*z - s2*w, s2*z + c2*w)

def update(h, a, b):
    fig.clear()
    points = iter.product([-1, 1], repeat=4)
    for p in points:
        x, y, z, w = p  
        rx, ry, rz, rw = rotate(p, a, b)
        dest = [rotate((-x, y, z, w), a, b), rotate((x, -y, z, w), a, b), 
                rotate((x, y, -z, w), a, b), rotate((x, y, z, -w), a, b)]
        sf = np.divide(h, h-rw)  
        # Connecting vertex to the 4 neighbouring vertices
        for d in dest:
            dx, dy, dz, dw = d
            dsf = np.divide(h, h-dw)
            fig.plot([sf*rx, dsf*dx], [sf*ry, dsf*dy], [sf*rz, dsf*dz], c="red")

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
    label="Angle about zw plane",
    valmin=-5,
    valmax=5,
    valinit=0,
    valstep=0.1,
)
a_slider.on_changed(lambda x : update(h_slider.val, x, b_slider.val))

b_slider = Slider(
    ax=plt.axes([0.2, 0.25, 0.65, 0.03]),
    label="Angle about xy plane",
    valmin=-5,
    valmax=5,
    valinit=0,
    valstep=0.1,
)
b_slider.on_changed(lambda x : update(h_slider.val, a_slider.val, x))

update(5, 0, 0)
plt.show()





