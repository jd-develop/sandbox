# coding:utf-8
import time
import py5
import os
from datetime import datetime
from random import randint


SQ_SIZE = 20
SQ_SHIFT = 10
offset = time.timezone if (time.localtime().tm_isdst == 0) else time.altzone
offset *= -1
week = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]


def setup():
    py5.size(1366, 748)
    py5.window_title("Décompte")
    py5.text_size(20)
    if os.path.exists("font.ttf"):
        font = py5.create_font("font.ttf", 100)
        py5.text_font(font)

def draw():
    py5.background(0)
    if py5.frame_count % 30 == 0:
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        while (r+g+b)//3 < 128:
            r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        py5.fill(r, g, b)
    # u_time_int = int(time.time()) + target - a 
    u_time_int = int(time.time())

    # exact date (local time)
    u_time_int += offset
    minutes, seconds = u_time_int // 60, u_time_int % 60
    hours, minutes = minutes // 60, minutes % 60
    days, hours = hours // 24, hours % 24

    day_in_week = (days+11) % 7

    year = 1970
    days += 1
    while True:
        is_leap_ = is_leap(year)
        if is_leap_ and days > 366:
            days -= 366
        elif days > 365:
            days -= 365
        else:
            break
        year += 1

    month = 1
    while True:
        if month in [1, 3, 5, 7, 8, 10, 12] and days > 31:
            days -= 31
        elif month in [4, 6, 9, 11] and days > 30:
            days -= 30
        elif month == 2 and is_leap_ and days > 29:
            days -= 29
        elif month == 2 and not is_leap_ and days > 28:
            days -= 28
        else:
            break
        month += 1

    offset_minutes = offset/60
    offset_hours = offset_minutes // 60
    offset_minutes = offset_minutes % 60
    if offset_hours < 0 and offset_minutes != 0:
        offset_hours += 1
    sign = '+' if offset_hours >= 0 else '-'

    if offset_minutes == 0 and offset_hours == 0:
        offset_str = ""
    elif offset_hours != 0 and offset_minutes == 0:
        offset_str = f"{sign}{abs(int(offset_hours))}"
    else:
        offset_str = f"{sign}{abs(int(offset_hours))}h{abs(int(offset_minutes))}"

    year = datetime.now().year
    next_new_year = datetime(year+1, 1, 1, 0, 0, 0)
    delta = next_new_year - datetime.now()
    delta_seconds = int(delta.total_seconds()) + 1

    py5.text_size(100)
    py5.text(f"{week[day_in_week]} "
             f"{year}-"
             f"{'0' if len(str(month)) == 1 else ''}{month}-"
             f"{'0' if len(str(days)) == 1 else ''}{days} "
             f"{'0' if len(str(hours)) == 1 else ''}{hours}:"
             f"{'0' if len(str(minutes)) == 1 else ''}{minutes}:"
             f"{'0' if len(str(seconds)) == 1 else ''}{seconds}", 50, 250)
    # py5.text_size(50)
    py5.text(f"{delta_seconds}", 575, 400)
    py5.text_size(20)
    py5.text(f"(UTC{offset_str})", 650, 550)



def is_leap(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)


py5.run_sketch()
