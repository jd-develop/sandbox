#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from board import Board


def main():
    user_rows = int(input("How many rows? "))
    while not isinstance(user_rows, int):
        print('Please enter integer.')
        user_rows = int(input("How many rows? "))
    user_columns = int(input("How many columns? "))
    while not isinstance(user_columns, int):
        print('Please enter integer.')
        user_columns = int(input("How many columns? "))

    game_board = Board(user_rows, user_columns)

    gen = 1
    game_board.draw_board()
    print(f"gen {gen}")

    user_action = ''
    while user_action != 'q':
        user_action = input('Press enter to add a generation, 10 to add 10 gens or q to quit: ')

        if user_action == '':
            gen += 1
            game_board.update_board()
            game_board.draw_board()
            print(f"gen {gen}")
        elif user_action == '10':
            for loop in range(10):
                gen += 1
                game_board.update_board()
                game_board.draw_board()
                print(f"gen {gen}")


main()
