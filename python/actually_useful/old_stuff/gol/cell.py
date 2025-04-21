#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Cell:
    def __init__(self):
        self.status = 'dead'

    def set_dead(self):
        self.status = 'dead'

    def set_alive(self):
        self.status = 'alive'

    def is_alive(self) -> bool:
        return self.status == 'alive'

    def return_print_char(self) -> str:
        return 'O' if self.is_alive() else ' '
