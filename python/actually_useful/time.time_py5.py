# coding:utf-8
import time
import py5


SQ_SIZE = 20
SQ_SHIFT = 10
offset = time.timezone if (time.localtime().tm_isdst == 0) else time.altzone
offset *= -1
week = ["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def setup():
    py5.size(700, 400)
    py5.window_title("Unix time")
    py5.text_size(20)


def draw():
    py5.background(0)
    py5.fill(255)
    u_time_int = int(time.time())
    unix_time_bin = bin(u_time_int)[2:]
    py5.text(f"Current Unix Time is {len(unix_time_bin)} bits long. It is:", 10, 20)
    py5.text(unix_time_bin, 10, 40)
    py5.text(f"Which is {u_time_int} in decimal, and 0x{hex(u_time_int)[2:].upper()} in hexadecimal.",
             10, 60)

    for i in range(64):
        index = len(unix_time_bin)-abs(i-63)-1
        is_1 = 0 <= index < len(unix_time_bin) and unix_time_bin[index] == "1"
        if is_1:
            r, g, b = 0, 0, 255
        else:
            r, g, b = 100, 100, 100
        py5.fill(r, g, b)
        x = (i % 16)
        y = (i // 16)
        py5.rect(x*(SQ_SIZE+SQ_SHIFT) + 10, y*(SQ_SIZE+SQ_SHIFT) + 80, SQ_SIZE, SQ_SIZE)

    py5.fill(255)
    text_y = 100+4*(SQ_SIZE+SQ_SHIFT)

    minutes, seconds = u_time_int // 60, u_time_int % 60
    hours, minutes = minutes // 60, minutes % 60
    days, hours = hours // 24, hours % 24

    day_is_plural = days > 1
    hour_is_plural = hours > 1
    minute_is_plural = minutes > 1
    second_is_plural = seconds > 1

    py5.text("Since 1/1/1970 00:00:00 UTC, exactly", 10, text_y)
    py5.text(f"{days} day{'s' if day_is_plural else ''}, "
             f"{hours} hour{'s' if hour_is_plural else ''}, "
             f"{minutes} minute{'s' if minute_is_plural else ''} and "
             f"{seconds} second{'s' if second_is_plural else ''} have elapsed.", 10, text_y+20)

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
    sign = '+' if offset_hours >= 0 else '-'

    if offset_minutes == 0 and offset_hours == 0:
        offset_str = ""
    elif offset_hours != 0 and offset_minutes == 0:
        offset_str = f"{sign}{abs(int(offset_hours))}"
    else:
        offset_str = f"{sign}{abs(int(offset_hours))}h{abs(int(offset_minutes))}"

    py5.text(f"Local time (UTC{offset_str}) is therefore "
             f"{week[day_in_week]} "
             f"{'0' if len(str(days)) == 1 else ''}{days}/"
             f"{'0' if len(str(month)) == 1 else ''}{month}/"
             f"{year} "
             f"{'0' if len(str(hours)) == 1 else ''}{hours}:"
             f"{'0' if len(str(minutes)) == 1 else ''}{minutes}:"
             f"{'0' if len(str(seconds)) == 1 else ''}{seconds}", 10, text_y+40)


def is_leap(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)


py5.run_sketch()
