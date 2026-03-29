from manim import *
import numpy as np


class KleinBottle(ThreeDScene):
    def klein(self, u, v):
        # Parametrization (matches the formula you showed)
        x = -(4 - 2 * np.cos(u)) * np.cos(v) + 6 * (np.sin(u) + 1) * np.cos(u)
        y = 16 * np.sin(u)
        z = (4 - 2 * np.cos(u)) * np.sin(v)
        return np.array([x, y, z]) * 0.08  # global scale to fit frame

    def construct(self):
        self.camera.background_color = BLACK

        # Fixed title
        title = Text("Klein Bottle").scale(1.1).to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)

        # Fixed equations (requires LaTeX installed + on PATH)
        eqs = VGroup(
            MathTex(r"x = -(4 - 2\cos u)\cos v + 6(\sin u + 1)\cos u"),
            MathTex(r"y = 16\sin u"),
            MathTex(r"z = (4 - 2\cos u)\sin v"),
        ).arrange(DOWN, buff=0.2).scale(0.6).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(eqs)

        # Subtle axes
        axes = ThreeDAxes(
            x_range=[-6, 6, 2],
            y_range=[-6, 6, 2],
            z_range=[-6, 6, 2],
        )
        axes.set_stroke(opacity=0.35, width=2)
        self.add(axes)

        # Surface (Manim CE v0.19 uses Surface, not ParametricSurface)
        surf = Surface(
            lambda u, v: self.klein(u, v),
            u_range=(0, TAU),
            v_range=(0, TAU),
            resolution=(48, 72),
        )
        surf.set_fill(color=PINK, opacity=0.75)
        surf.set_stroke(color=YELLOW, width=1.0, opacity=0.9)

        # Portable "mesh": draw parameter lines (no SurfaceMesh dependency)
        u_lines = VGroup()
        v_lines = VGroup()

        for u0 in np.linspace(0, TAU, 13):  # constant-u curves
            curve = ParametricFunction(
                lambda t, u0=u0: self.klein(u0, t),
                t_range=(0, TAU),
            )
            curve.set_stroke(WHITE, width=1, opacity=0.35)
            u_lines.add(curve)

        for v0 in np.linspace(0, TAU, 19):  # constant-v curves
            curve = ParametricFunction(
                lambda t, v0=v0: self.klein(t, v0),
                t_range=(0, TAU),
            )
            curve.set_stroke(WHITE, width=1, opacity=0.25)
            v_lines.add(curve)

        grid = VGroup(u_lines, v_lines)

        # Camera framing
        self.set_camera_orientation(phi=70 * DEGREES, theta=-35 * DEGREES, zoom=1.2)

        # Animation
        self.play(FadeIn(surf), FadeIn(grid), run_time=2)
        self.begin_ambient_camera_rotation(rate=0.12)
        self.wait(6)
        self.stop_ambient_camera_rotation()
        self.wait(1)
