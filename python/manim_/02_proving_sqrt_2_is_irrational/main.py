# coding:utf-8
from manim import *


class Sqrt2IsIrrational(Scene):
    def construct(self):
        main_text = Tex("Supposons ", r"$\sqrt{2}$", " rationnel.")
        text1 = Tex(r"$\sqrt{2} = \frac{a}{b}$; $a, b \in \mathbb{N}$; $\frac{a}{b}$ la fraction la plus simplifiée.")

        text2 = MathTex(r"\sqrt{2} = \frac{a}{b}")
        text3 = MathTex(r"\frac{a^2}{b^2} = 2")
        text4 = MathTex(r"a^2 = 2b^2; b^2 \in \mathbb{N}")
        text5 = Tex("$a$ est donc pair.")

        text6 = MathTex(r"\sqrt{2} = \frac{a}{b}")
        text7 = MathTex(r"\frac{a^2}{b^2} = 2")
        text8 = MathTex(r"a^2 = 2b^2; a = 2m; m \in \mathbb{N}")
        text9 = MathTex(r"(2m)^2 = 2b^2")
        text10 = MathTex(r"4m^2 = 2b^2")
        text11 = MathTex(r"2m^2 = b^2; m^2 \in \mathbb{N}")
        text12 = Tex("$b$ est donc pair.")

        text13 = MathTex(r"\sqrt{2} = \frac{a}{b}")
        text14 = Tex(r"$\sqrt{2} = \frac{a}{b}$; a et b divisibles par 2.")
        text15 = Tex(r"La fraction ", r"$\frac{a}{b}$", " supposée simplifiée ne l’est en fait pas.")
        text16 = Tex(r"Le raisonnement ne tient pas, ", r"$\sqrt{2}$ est irrationnel.")
        rect = SurroundingRectangle(text16[1])
        self.play(Create(main_text))
        self.play(Wait(2))
        self.play(Transform(main_text, text1))
        self.play(Wait(5))
        self.play(Transform(main_text, text2))
        self.play(Wait(1))
        self.play(Transform(main_text, text3))
        self.play(Wait(1))
        self.play(Transform(main_text, text4))
        self.play(Wait(2))
        self.play(Transform(main_text, text5))
        self.play(Wait(5))
        self.play(Transform(main_text, text6))
        self.play(Wait(1))
        self.play(Transform(main_text, text7))
        self.play(Wait(1))
        self.play(Transform(main_text, text8))
        self.play(Wait(2))
        self.play(Transform(main_text, text9))
        self.play(Wait(1))
        self.play(Transform(main_text, text10))
        self.play(Wait(1))
        self.play(Transform(main_text, text11))
        self.play(Wait(2))
        self.play(Transform(main_text, text12))
        self.play(Wait(5))
        self.play(Transform(main_text, text13))
        self.play(Wait(1))
        self.play(Transform(main_text, text14))
        self.play(Wait(3))
        self.play(Transform(main_text, text15))
        self.play(Wait(3))
        self.play(Transform(main_text, text16))
        self.play(Create(rect))
        self.play(Wait(8))
        self.play(FadeOut(main_text), FadeOut(rect))
        self.wait()
