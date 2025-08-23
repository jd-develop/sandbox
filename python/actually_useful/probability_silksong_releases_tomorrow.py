#!/usr/bin/env python3
# coding:utf-8
import datetime

reveal_date = datetime.date(2019, 2, 14)
today = datetime.date.today()
june12 = datetime.date(2023, 6, 12)
september18 = datetime.date(2025, 9, 18)
september4 = datetime.date(2025, 9, 4)

delta = (september4-today).days

probability = int(delta == 1)

print(f"Cela fait {(today-reveal_date).days} jours que Hollow Knight: Silksong a été annoncé.")
print("Il a été annoncé que Hollow Knight: Silksong sortira le 4 septembre 2025.")
print(f"Il reste donc {delta} jours, et Silksong sortira demain avec une probabilité de {probability}.")
