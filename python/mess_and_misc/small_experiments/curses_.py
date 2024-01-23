#!/urs/bin/env python3
# -*- coding:utf-8 -*-
import curses
from curses import wrapper
import time


def main(stdscr):
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)
    curses.init_pair(2, -1, curses.COLOR_GREEN)

    stdscr.clear()
    stdscr.refresh()

    stdscr.addstr("This text is         .", curses.A_DIM)
    stdscr.addstr(0, 13, "blinking", curses.A_BLINK | curses.A_BOLD)
    stdscr.addstr(5, 5, "Hello world!", curses.A_BOLD)
    stdscr.addstr(10, 5, "Hello world!", curses.A_UNDERLINE)
    stdscr.addstr(11, 5, "Hello world!", curses.color_pair(1) | curses.A_ITALIC)

    stdscr.getkey()

    counter_window = curses.newwin(1, 20, 10, 10)

    # stdscr.clear()
    for i in range(20):
        counter_window.clear()

        counter_window.addstr(str(i), curses.color_pair(i%2 + 1))
        counter_window.refresh()
        time.sleep(0.1)
    
    stdscr.refresh()
    stdscr.getkey()


def pad_main(stdscr):
    pad = curses.newpad(1, 68)
    stdscr.refresh()
    pad.addstr("Ceci est un texte défilant assez rapidement et revenant en arrière.")

    for _ in range(3):
        stdscr.clear()
        stdscr.refresh()

        pad.refresh(0, 0, 5, 5, 6, 25)
        time.sleep(1)
        for i in range(68-20):
            stdscr.clear()
            stdscr.refresh()
            pad.refresh(0, i, 5, 5+i, 6, 25+i)
            time.sleep(0.05)

        time.sleep(1)
        for i in range(68-21, -1, -1):
            stdscr.clear()
            stdscr.refresh()
            pad.refresh(0, i, 5, 5+i, 6, 25+i)
            time.sleep(0.05)

    stdscr.getch()


def user_input(stdscr):
    curses.use_default_colors()
    line_count = 1
    while True:
        key = stdscr.getkey()
        if key == "\n":
            break
        if line_count >= curses.LINES:
            stdscr.clear()
            line_count = 1
        stdscr.addstr(f"You typed: {key}, line_count is {line_count}, LINES is {curses.LINES}\n")
        line_count += 1
        stdscr.refresh()


wrapper(user_input)
