#!/usr/bin/env python3
# coding:utf-8
import datetime

reveal_date = datetime.date(2019, 2, 14)
today = datetime.date.today()
june12 = datetime.date(2023, 6, 12)
_2025 = datetime.date(2025, 12, 25)
september18 = datetime.date(2025, 9, 18)
june6 = datetime.date(2025, 6, 6)

delta = (_2025-today).days
delta2 = (september18-today).days

probability = 100/delta
probability2 = 100/delta2

print(f"Cela fait {(today-reveal_date).days} jours que Hollow Knight: Silksong a été annoncé.")
print()
print("Il a été annoncé que Hollow Knight: Silksong sortira avant la fin 2025, i.e. avant le 25 décembre 2025 inclus.")
print(f"Il y a donc une chance sur {delta} que Hollow Knight: Silksong sorte demain, soit {probability}% de probabilité.")
print()
print("De plus, il est conjecturé que Hollow Knight: Silksong sortira avant le 18 septemble 2025 inclus.")
print(f"Dans ce cas, il y a une chance sur {delta2} que Hollow Knight: Silksong sorte demain, soit {probability2}% de probabilité.")
