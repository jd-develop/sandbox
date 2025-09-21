#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from fractions import Fraction


class _Fraction(Fraction):
    def __repr__(self):
        if self.is_integer():
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"
    
    def __str__(self):
        return repr(self)


def étage(p: int, étage_p_moins_1: list[_Fraction] | None = None) -> list[_Fraction]:
    assert p >= 0, "p doit être positif ou nul"
    if p == 0:
        return [_Fraction(1, 1)]
    if étage_p_moins_1 is None:
        étage_p_moins_1 = étage(p-1)
    
    étage_p: list[_Fraction] = []
    for i in range(len(étage_p_moins_1)):
        if i == 0:
            étage_p.append(_Fraction(
                étage_p_moins_1[i].numerator,
                étage_p_moins_1[i].denominator + 1
            ))
        else:
            étage_p.append(_Fraction(
                étage_p_moins_1[i-1].numerator + étage_p_moins_1[i].numerator,
                étage_p_moins_1[i-1].denominator + étage_p_moins_1[i].denominator
            ))
        étage_p.append(étage_p_moins_1[i])
    étage_p.append(_Fraction(
        étage_p_moins_1[len(étage_p_moins_1)-1].numerator + 1,
        étage_p_moins_1[len(étage_p_moins_1)-1].denominator
    ))
    return étage_p


arbre: list[list[_Fraction]] = []
for j in range(10):
    if j == 0:
        arbre.append(étage(0))
        continue
    arbre.append(étage(j, arbre[-1]))    


print(arbre)
