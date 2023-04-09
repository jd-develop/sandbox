#!/usr/bin/env python3
# coding:utf-8
import datetime

reveal_date = datetime.date(2019, 2, 14)
today = datetime.date.today()
june12 = datetime.date(2023, 6, 12)

delta = (june12-today).days

probability = 100/delta

print(f"Cela fait {(today-reveal_date).days} jours que Hollow Knight: Silksong a été annoncé.")
print(f"Il y a une chance sur {delta} que Hollow Knight: Silksong sorte demain, soit {probability}% de probabilité.")
