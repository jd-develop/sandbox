# coding:utf-8
from manim import *


class HelloWorld(Scene):
    def construct(self):
        hello = Text("Hello World!")

        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.rotate(PI/4)

        self.play(Write(hello))
        self.play(FadeOut(hello))

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

        square = Square()
        square.rotate(PI / 4)
        text = Text("manim is super cool!")

        self.play(FadeIn(text))
        self.play(Transform(text, circle))
        self.play(Transform(text, square))
        self.play(Transform(text, Text("wow!")))
        self.play(FadeOut(text))
        self.wait()


class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.set_fill(BLUE, opacity=0.5)

        triangle = Triangle()
        triangle.set_fill(YELLOW, opacity=0.5)

        square.next_to(circle, RIGHT, buff=2)
        triangle.next_to(circle, LEFT, buff=2)

        new_triangle = Triangle()
        new_triangle.set_fill(BLUE, opacity=0.5)
        new_square = Square()
        new_square.set_fill(YELLOW, opacity=0.5)

        new_triangle.next_to(circle, RIGHT, buff=2)
        new_square.next_to(circle, LEFT, buff=2)

        self.play(Create(circle), Create(square), Create(triangle))
        self.play(FadeOut(circle), Transform(square, new_triangle), Transform(triangle, new_square))
        self.play(FadeOut(triangle), FadeOut(square))


class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(Create(square))
        self.play(square.animate.rotate(PI/4))
        self.play(ReplacementTransform(square, circle))
        self.play(circle.animate.set_fill(PINK, opacity=0.5))


class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(left_square.animate.rotate(PI/2), Rotate(right_square, angle=PI/2), run_time=2)
        self.wait()
