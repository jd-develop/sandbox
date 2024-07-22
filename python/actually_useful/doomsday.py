#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from datetime import datetime
import random
import time

DAYS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]


def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def month_duration(month: int, year: int):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 30


score = 0
best = 999999

while True:
    year = random.randint(1800, 2199)
    month = random.randint(1, 12)
    day = random.randint(1, month_duration(month, year))
    random_date = datetime(year, month, day)
    day_of_week = DAYS[random_date.weekday()]

    debut = time.time()
    answer = input(f"{year}-{month}-{day}: ").lower()
    if answer == day_of_week:
        print("oui !")
        score += 1
        temps = int(time.time()-debut)
        print(f"Réponse en {temps}s.")
        if temps < best:
            best = temps
            print("Nouveau meilleur temps !")
    else:
        print(f"non, c’était {day_of_week}")
        score -= 2
    print(f"Score: {score}")
    print()

