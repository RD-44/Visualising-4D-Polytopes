from manim import *
import itertools as iter

class cube(ThreeDScene):
    def construct(self):


    
        # Setup axes
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

        # Add dot and cube
        h=ValueTracker(2.5)
        dot = Dot3D([0, 0, h.get_value()], radius=0.1, color=RED)
        self.add(axes, dot)
        cube = Cube(side_length=1, fill_opacity=0.25, fill_color=ORANGE, stroke_width=0.3)
        cube2 = Cube(side_length=1, fill_opacity=0.25, fill_color=ORANGE, stroke_width=0.3)
        self.add(axes, cube)
        self.add(axes, cube2)
        self.move_camera(phi=60 * DEGREES)
        self.wait()

        # phi rotates camera out of the screen x rads backward
        # theta rotates camera pi/2+x rads to the right
        # gamma rotates camera x rads clockwise
        #self.move_camera(phi=-90 * DEGREES)
        

        self.begin_ambient_camera_rotation(
            rate=PI/10, about="theta"
        )
        
        def func(point, k):
            x, y, z = point
            sf = np.divide(k, k-z)
            return [sf*x, sf*y, 0]
        
        def updater(obj):
            ApplyPointwiseFunction(function=lambda p : func(p, obj.get_value()), mobject=cube)

        h.add_updater(updater)

        self.play(ApplyPointwiseFunction(function=lambda p : func(p, h.get_value()), mobject=cube))
        self.wait(1)
        self.play(h.animate.set_value(5))

        self.stop_ambient_camera_rotation()
        

