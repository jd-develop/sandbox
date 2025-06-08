#!/usr/bin/env python3
# coding:utf-8
import datetime

reveal_date = datetime.date(2019, 2, 14)
today = datetime.date.today()
june12 = datetime.date(2023, 6, 12)
_2025 = datetime.date(2025, 12, 31)
september18 = datetime.date(2025, 9, 18)
june6 = datetime.date(2025, 6, 6)

delta = (_2025-today).days
delta2 = (september18-today).days
delta3 = (today-june6).days

probability = 100/delta if delta3 >= 0 else 0
probability2 = 100/delta2 if delta3 >= 0 else 0

print(f"Cela fait {(today-reveal_date).days} jours que Hollow Knight: Silksong a été annoncé.")
print()
print("Il a été annoncé que Hollow Knight: Silksong sortira en 2025, i.e. avant le 31 décembre 2025 inclus.")
print("On sait également que Hollow Knight: Silksong sortira après le 6 juin 2025.")
if delta3 >= 0:
    print(f"Il y a donc une chance sur {delta} que Hollow Knight: Silksong sorte demain, soit {probability}% de probabilité.")
    print()
    print("De plus, il est conjecturé que Hollow Knight: Silksong sortira avant le 18 septemble 2025 inclus.")
    print(f"Dans ce cas, il y a une chance sur {delta2} que Hollow Knight: Silksong sorte demain, soit {probability2}% de probabilité.")
else:
    print("Il y a donc 0% de probabilité que Hollow Knight: Silksong sorte demain.")
