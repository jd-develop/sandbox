import pprint

l_ = ["1"]

loop = int(input("How many terms should be calculated?\nIt starts being slow around ~40/50 and completely filling the "
                 "Ubuntu terminal app at 45.\nRecommended value: 44.\n>"))

for i in range(loop):
    a = l_[-1]
    b = ""
    enum_ = 0
    current_num = a[0]
    for c in a:
        if c == current_num:
            enum_ += 1
        else:
            b += str(enum_) + current_num
            current_num = c
            enum_ = 1
    b += str(enum_) + current_num
    l_.append(b)

pprint.pprint(l_)
