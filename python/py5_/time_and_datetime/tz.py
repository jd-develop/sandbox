# coding:utf-8
import time
import py5

week = ["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

offsets = [-12, 0, +2, +14]
offsets = [o*3600 for o in offsets]


def setup():
    py5.size(700, 400)
    py5.window_title("Timezones")
    py5.text_size(20)


def draw():
    py5.background(0)
    py5.fill(255)
    u_time_int = int(time.time())
    py5.text(f"Current Unix time is {u_time_int}.", 10, 20)

    y = 40
    for offset in offsets:
        u_time_offset = u_time_int + offset
        minutes, seconds = u_time_offset // 60, u_time_offset % 60
        hours, minutes = minutes // 60, minutes % 60
        days, hours = hours // 24, hours % 24

        day_in_week = (days + 11) % 7

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

        offset_minutes = offset / 60
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

        py5.text(f"UTC{offset_str} is "
                 f"{week[day_in_week]} "
                 f"{'0' if len(str(days)) == 1 else ''}{days}/"
                 f"{'0' if len(str(month)) == 1 else ''}{month}/"
                 f"{year} "
                 f"{'0' if len(str(hours)) == 1 else ''}{hours}:"
                 f"{'0' if len(str(minutes)) == 1 else ''}{minutes}:"
                 f"{'0' if len(str(seconds)) == 1 else ''}{seconds}", 10, y)
        y += 20


def is_leap(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)


py5.run_sketch()
