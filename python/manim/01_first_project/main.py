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
        self.play(Transform(text, Text("Look at those squares!")))
        self.play(FadeOut(text))


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
