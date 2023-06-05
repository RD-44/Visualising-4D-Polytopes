from manim import *
import itertools as iter

class Tes(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-4, 4, 1],
            z_axis_config={"include_numbers": True},
            y_axis_config={"include_numbers": True},
            x_axis_config={"include_numbers": True},
            x_length=8,
            y_length=8,
            z_length=8,
        )
        labels = axes.get_axis_labels(Tex("x").scale(0.7), Tex("y").scale(0.7), Tex("z").scale(0.7))
        axes.add(labels)
        self.move_camera(phi=60 * DEGREES)

        self.begin_ambient_camera_rotation(
            rate=PI/10, about="theta"
        )

        h=2
        points = iter.product([-1, 1], repeat=4)
        for p in points:
            x, y, z, w = p
            sf = (h/(h-w))
            wsf = (h/(h+w))
            nx = sf*x
            ny = sf*y
            nz = sf*z
            self.add(axes, Line3D(start=np.array([nx, ny, nz]), end=np.array([-nx, ny, nz])))
            self.add(axes, Line3D(start=np.array([nx, ny, nz]), end=np.array([nx, -ny, nz])))
            self.add(axes, Line3D(start=np.array([nx, ny, nz]), end=np.array([nx, ny, -nz])))
            self.add(axes, Line3D(start=np.array([nx, ny, nz]), end=np.array([wsf*x, wsf*y, wsf*z])))
                
        self.wait(3)

        self.stop_ambient_camera_rotation()