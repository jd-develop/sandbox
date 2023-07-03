# coding:utf-8
# messing around with monty hall problem and statistics
import random


def monty_hall(change_door: bool = False, doors: int = 3):
    winning_door = random.randint(0, 2)
    choice = random.randint(0, 2)
    reveal = random.randint(0, 2)
    while reveal == choice or reveal == winning_door:
        reveal = random.randint(0, 2)
    if change_door:  # i’m sure there’s a way to optimize that — if this is the case, let me know :)
        if choice == 0:
            if reveal == 1:
                choice = 2
            else:
                choice = 1
        elif choice == 1:
            if reveal == 0:
                choice = 2
            else:
                choice = 0
        else:
            if reveal == 0:
                choice = 1
            else:
                choice = 0
    return choice == winning_door


# not changing door
result = []
for i in range(1000):
    result.append(int(monty_hall(False)))

print(f"not changing: win={sum(result)*100/len(result)}%")


# changing door
result = []
for i in range(1000):
    result.append(int(monty_hall(True)))

print(f"    changing: win={sum(result)*100/len(result)}%")
