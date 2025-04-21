#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
from cell import Cell


class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = [[Cell() for column_cell in range(self.columns)] for row_cells in range(self.rows)]

        self.generate_board()

    def generate_board(self):
        for row in self.grid:
            for cell in row:
                chance_number = random.randint(0, 2)
                if chance_number == 1:
                    cell.set_alive()

    def draw_board(self):
        print('\n'*10)
        print("Printing board")
        for row in self.grid:
            for cell in row:
                print(cell.return_print_char(), end='')
            print()  # creates a new line

    def check_neighbour(self, x, y):
        search_min = -1
        search_max = 2

        neighbour = []
        for row in range(search_min, search_max):
            for cell in range(search_min, search_max):
                neighbour_row = x + row
                neighbour_cell = y + cell

                valid_neighbour = True

                if neighbour_row == x and neighbour_cell == y:
                    valid_neighbour = False

                if neighbour_row < 0 or neighbour_row >= self.rows:
                    valid_neighbour = False

                if neighbour_cell < 0 or neighbour_cell >= self.columns:
                    valid_neighbour = False

                if valid_neighbour:
                    neighbour.append(self.grid[neighbour_row][neighbour_cell])
        return neighbour

    def update_board(self):
        print('updating board')
        goes_alive = []
        get_killed = []

        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                check_neighbour = self.check_neighbour(row, column)

                living_neighbour_count = 0

                for neighbour_cell in check_neighbour:
                    if neighbour_cell.is_alive():
                        living_neighbour_count += 1

                cell_object = self.grid[row][column]
                is_main_cell_alive = cell_object.is_alive()

                if is_main_cell_alive:
                    if living_neighbour_count < 2 or living_neighbour_count > 3:
                        get_killed.append(cell_object)
                    if living_neighbour_count == 3 or living_neighbour_count == 2:
                        goes_alive.append(cell_object)
                else:
                    if living_neighbour_count == 3:
                        goes_alive.append(cell_object)

        for cell_items in goes_alive:
            cell_items.set_alive()
        for cell_items in get_killed:
            cell_items.set_dead()
