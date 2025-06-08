#!/usr/bin/env python3
# coding:utf-8
import datetime

reveal_date = datetime.date(2019, 2, 14)
today = datetime.date.today()
june12 = datetime.date(2023, 6, 12)
september18 = datetime.date(2025, 9, 18)
june6 = datetime.date(2025, 6, 6)

delta2 = (september18-today).days

probability2 = 100/delta2

print(f"Cela fait {(today-reveal_date).days} jours que Hollow Knight: Silksong a été annoncé.")
print()
print("Il a été annoncé que Hollow Knight: Silksong sortira pendant l’été 2025, et il y a")
print("des raisons de penser qu’il sortira avant le 18 septembre 2025 inclus.")

print(f"Il y a donc une chance sur {delta2} que Hollow Knight: Silksong sorte demain, soit {probability2}% de probabilité.")
