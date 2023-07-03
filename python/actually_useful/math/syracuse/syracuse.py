# coding:utf-8
import pathlib

print("Reading file...", end=" ")
path = pathlib.Path(__file__).parent.absolute()
with open(f"{path}/loop_on_421", "r+", encoding="UTF-8") as f:
    loop_on_421 = f.readlines()

print("Done.")
print("Converting to int...", end=" ")
loop_on_421 = [int(n) for n in loop_on_421]
print("Done.")

for i in range(100000, 105000):
    if i in loop_on_421:
        print(f"Continue for {i}...")
        continue
    values = [i]
    n = i
    print(n, end="")

    while n != 1:
        print("->", end="")
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        print(n, end="")
        if n in loop_on_421:
            break
        values.append(n)

    print()
    loop_on_421.extend(values)

print("Sorting...", end=" ")
loop_on_421.sort()
print("Done.")
print("Writing in file...", end=" ")
with open(f"{path}/loop_on_421", "w+", encoding="UTF-8") as f:
    for n in loop_on_421:
        f.write(str(n) + "\n")
print("Done.")
