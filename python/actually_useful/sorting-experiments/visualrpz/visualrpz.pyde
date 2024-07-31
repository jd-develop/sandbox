from random import shuffle, randint

# Things you can change 
mode = ["LINEAR", "RANDOMIZED"][0]
lenght = 50
algorithm = ["bubble", "selection", "insertion", "bozo"][0]
framerate = 100
colors = True

# Initialize the list
if mode == "LINEAR":
    original_list = [i for i in range(lenght)]
    shuffle(original_list)  # randomize
else:
    original_list = [randint(0, lenght) for i in range(lenght)]

sorted_list = list(original_list)

# Initialize useful stuff
BUBBLE = algorithm == "bubble"
SELECTION = algorithm == "selection"
INSERTION = algorithm == "insertion"
MERGE = algorithm == "merge"
BOZO = algorithm == "bozo"

sorted_count = 0
sorting = True
if MERGE:
    what_to_do_next = "splitting"
else:
    what_to_do_next = "comparing"
context = []
if algorithm in ["insertion"]:
    check_i = 1
else:
    check_i = 0
sub_arrays_indexes = []

width_unit = height_unit = 0
delay(100)


def setup():
    global width_unit, height_unit, algorithm, framerate
    # window size
    size(900, 650)
    # frame rate
    frameRate(framerate)
    # width and height of the rectangles
    width_unit = width//len(original_list)
    height_unit = height//max(original_list)
    background(0)


def update_view(list_):
    """Update graphics"""
    global context
    clear()
    background(0)
    for i in range(len(list_)):
        if colors:
            if len(context) >= 1 and i == context[0]:
                fill(255, 0, 0)
            elif len(context) >= 2 and i == context[1]:
                fill(0, 255, 0)
            elif len(context) >= 3 and i == context[2]:
                fill(0, 0, 255)
            elif i in context and i not in context[:3]:
                fill(0, 255, 0)
        rect(i*width_unit, height, width_unit, -list_[i]*height_unit)
        fill(255)


def draw():
    global sorted_list, sorting, sorted_count, what_to_do_next, context, check_i, lenght
    update_view(sorted_list)
    
    if sorting:
        if BUBBLE:
            bubble_sort()
        elif SELECTION:
            selection_sort()
        elif INSERTION:
            insertion_sort()
        elif BOZO:
            # BOZO SORT
            sorted_ = True
            for i in range(len(sorted_list)-1):
                if sorted_list[i] > sorted_list[i+1]:
                    sorted_ = False
            if sorted_:
                sorting = False
            else:
                shuffle(sorted_list)
    else:
        if len(context) <= 3:
            context = [lenght+1, lenght+1, lenght+1, 0]
        else:
            context.append(context[-1]+1)
                
def bubble_sort():
    global sorted_list, sorting, sorted_count, what_to_do_next, context, check_i
    # BUBBLE SORT
    if what_to_do_next == "comparing":
        if sorted_count+1 < len(sorted_list):
            context = []
            # sorted count part de 0 jusqu'à la taille de la liste, or on a besoin d'une variable i qui va de la taille de la liste à 0
            i = len(sorted_list) - sorted_count
            if check_i+1 == i:
                check_i = 0
                context = []
                sorted_count += 1
            else:
                if sorted_list[check_i+1] < sorted_list[check_i]:
                    what_to_do_next = "swapping"
                context = [check_i, check_i+1]
                check_i += 1
        else:
            sorting = False
    else:
        sorted_list[context[0]], sorted_list[context[1]] = sorted_list[context[1]], sorted_list[context[0]]
        what_to_do_next = "comparing"


def selection_sort():
    global sorted_list, sorting, sorted_count, what_to_do_next, context, check_i
    # SELECTION SORT
    if what_to_do_next == "comparing":
        if sorted_count+1 < len(sorted_list):
            lowest_i = sorted_count
            next_is_swap = False
            if len(context) == 3:
                lowest_i = context[1]

            if sorted_list[check_i] < sorted_list[lowest_i]:
                lowest_i = check_i
            if check_i >= len(sorted_list)-1:
                next_is_swap = True
            
            context = [sorted_count, lowest_i, check_i]
            if next_is_swap:
                sorted_count += 1
                what_to_do_next = "swapping"
                check_i = sorted_count+1
            else:
                check_i += 1
        else:
            sorting = False
    else:
        sorted_list[context[0]], sorted_list[context[1]] = sorted_list[context[1]], sorted_list[context[0]]
        context = []
        what_to_do_next = "comparing"


def insertion_sort():
    global sorted_list, sorting, sorted_count, what_to_do_next, context, check_i
    # SELECTION SORT
    if what_to_do_next == "comparing":
        context = []
        if sorted_count < len(sorted_list):
            if check_i > 0 and sorted_list[check_i-1] > sorted_list[check_i]:
                what_to_do_next = "swapping"
                context = [check_i, check_i-1, sorted_count]
                check_i -= 1
            else:
                what_to_do_next = "comparing"
                sorted_count += 1
                check_i = sorted_count
        else:
            sorting = False
    else:
        sorted_list[context[0]], sorted_list[context[1]] = sorted_list[context[1]], sorted_list[context[0]]
        what_to_do_next = "comparing"
