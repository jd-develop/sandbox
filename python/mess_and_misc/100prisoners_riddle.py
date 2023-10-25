#!/urs/bin/env python3
# -*- coding:utf-8 -*-
import random

PRISONNERS_COUNT = 100
# first: "random" approach
suceed = 0
total = 0

for experiment in range(10000):
    boxes = list(range(PRISONNERS_COUNT))
    random.shuffle(boxes)

    failed = False
    for prisonner in range(PRISONNERS_COUNT):
        found = False
        already_did = []
        for attempt in range(int(PRISONNERS_COUNT/2)):
            i = random.randint(0, PRISONNERS_COUNT-1)
            while i in already_did:
                i = random.randint(0, PRISONNERS_COUNT-1)
            already_did.append(i)
            if boxes[i] == prisonner:
                found = True
                break
        if not found:
            failed = True
            break
    if not failed:
        suceed += 1
    total += 1

print(f"{suceed=}")
print(f"{total=}")
print(f"proportion: {suceed*100/total}%")


# "smarter" approach
suceed = 0
total = 0

for experiment in range(10000):
    boxes = list(range(PRISONNERS_COUNT))
    random.shuffle(boxes)

    failed = False
    for prisonner in range(PRISONNERS_COUNT):
        attempts_remaining = PRISONNERS_COUNT/2 - 1
        current_num = boxes[prisonner]
        while not (current_num == prisonner or attempts_remaining == 0):
            current_num = boxes[current_num]
            attempts_remaining -= 1
        if current_num != prisonner:
            failed = True
            break
    if not failed:
        suceed += 1
    total += 1

print(f"{suceed=}")
print(f"{total=}")
print(f"proportion: {suceed*100/total}%")

