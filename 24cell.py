import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import itertools as iter
import numpy as np
from math import sin, cos
# schleffel projection, look at other types 
# look at future possibilities as well as current stuff
# choosing the best hyperplanes for the projection, e.g 
# optimal angles for the planes
# gram-shmidt
# principal component analysis 
fig = plt.subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.25)

ones = iter.product([1, -1], repeat=2)
points = []
for x, y in ones:
    points.append((x, y, 0, 0))
    points.append((x, 0, 0, y))
    points.append((0, 0, x, y))
    points.append((x, 0, 0, y))
    points.append((x, 0, y, 0))
    points.append((0, x, 0, y))

def dist(p1, p2):
    return sum((p1[i]-p2[i])**2 for i in range (4))

def rotate(point, a, b): # Applies 4D rotation matrix
    x, y, z, w = point
    c1, s1, c2, s2 = cos(a), sin(a), cos(b), sin(b)
    return (c1*x - s1*y, s1*x + c1*y, c2*z - s2*w, s2*z + c2*w)

def update(h, a, b):
    fig.clear()
    for p in points:
        rx, ry, rz, rw = rotate(p, a, b)
        sf = np.divide(h, h-rw)  
        fig.scatter(sf*rx, sf*ry, sf*rz, c="red")
        
        for d in points:
            if dist(p, d) == 2:
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

