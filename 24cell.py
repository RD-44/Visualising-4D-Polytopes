import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import itertools as iter
import numpy as np
from math import sin, cos

fig = plt.subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.25)

# Constructing the 24 points for the 24-cell (side length sqrt(2))
ones = iter.product([1, -1], repeat=2)
points = []
for x, y in ones:
    points.append((x, y, 0, 0))
    points.append((x, 0, 0, y))
    points.append((0, 0, x, y))
    points.append((0, x, y, 0))
    points.append((x, 0, y, 0))
    points.append((0, x, 0, y))

def distsquared(p1, p2):
    return sum((p1[i]-p2[i])**2 for i in range (4))

# Creates an adjacency matrix to represent vertex connections in the shape
neighbours = {}
for p in points:
    neighbours[p] = set()
    for k in points:
        if distsquared(p, k) == 2 and not (k in neighbours and p in neighbours[k]):
            # Avoid duplicate connections between vertices for efficiency
            neighbours[p].add(k)

def rotate(point, a, b): # Applies 4D rotation matrix
    # a radians about the xy plane, b radians about the zw plane
    x, y, z, w = point
    c1, s1, c2, s2 = cos(a), sin(a), cos(b), sin(b)
    return (c1*x - s1*y, s1*x + c1*y, c2*z - s2*w, s2*z + c2*w)

# Draws the shape
def update(h, a, b):
    fig.clear()
    for p in points:
        x, y, z, w = rotate(p, a, b)
        sf = np.divide(h, h-w)  
        # fig.scatter(sf*x, sf*y, sf*z, c="red")
        # uncomment above to mark points for vertices
        for n in neighbours[p]:
            nx, ny, nz, nw = rotate(n, a, b)
            nsf = np.divide(h, h-nw) 
            fig.plot([sf*x, nsf*nx], [sf*y, nsf*ny], [sf*z, nsf*nz])

# Sliders to vary h, a, b are made below
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

